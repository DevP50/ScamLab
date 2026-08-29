from flask import Blueprint, render_template, redirect, url_for, flash, session,request
from forms import RegistrationForm,LoginForm
from app.models import User,Scenario,ScenarioDifficulty,Attempt
from extensions import db
from app.services.calculate_xp import calculate_xp
from app.services.calculate_score import calculate_score
from sqlalchemy import case
from werkzeug.security import generate_password_hash,check_password_hash
from . import auth_bp,app_bp


@app_bp.route('/')
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data.strip().lower() #Collecting data from the form
        password_hash = generate_password_hash(form.password.data)#Wrapping the password in a hashing algorithm
        if User.query.filter_by(email=email).first():
            flash("This email already exists please select a new one")
            return redirect(url_for('register'))

        new_user = User(
            username = username,
            email=email,
            password_hash=password_hash     
            )
        db.session.add(new_user)
        db.session.commit(new_user)
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, form.password.data):
          session['user'] = user.email
          flash('Login successful!', 'success')
          return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth_bp.login'))

    return render_template('login.html', form=form)

@auth_bp.route('/dashboard', methods=['GET','POST'])
def dashboard():
    user = User.query.all()
    return render_template('dashboard.html',user=user)



@auth_bp.route('/play', methods=['GET', 'POST'])
def start_training():
    user_answer = None
    correct = None
    message = None
    result = None
    selected_clues = None

    LEVEL_1_END = 5
    level_complete = False
    next_scenario = None

    difficulty_order = case(
        (Scenario.difficulty == ScenarioDifficulty.EASY, 1),
        (Scenario.difficulty == ScenarioDifficulty.MEDIUM, 2),
        (Scenario.difficulty == ScenarioDifficulty.HARD, 3)
    )

    # Debug: show all scenarios
    for s in Scenario.query.all():
        print(s.id, s.title, s.difficulty, s.difficulty.value)

    if request.method == "GET":

        # Check if we're supposed to load a specific next scenario
        next_id = request.args.get("next")

        if next_id:
            scenario = Scenario.query.get(next_id)
        else:
            # Start from the first scenario
            scenario = Scenario.query.order_by(
                difficulty_order,
                Scenario.id
            ).first()

        if not scenario:
            return "Scenario not found", 404

    else:
        # Get the scenario the user just answered
        scenario_id = request.form.get("scenario_id")
        scenario = Scenario.query.get(scenario_id)

        if not scenario:
            return "Scenario not found", 404

        user_answer = request.form.get('answer').lower()
        selected_clues = request.form.getlist('clues')

        print("USER ANSWER:", user_answer)
        print("CORRECT ANSWER:", scenario.correct_answer)
        print("SELECTED CLUES:", selected_clues)

        correct = (user_answer == scenario.correct_answer)

        result_xp = calculate_xp(
            correct_answer=correct,
            selected_clues=selected_clues,
            scenario_clues=scenario.clues
        )

        score = calculate_score(
            correct_answer=correct,
            selected_clues=selected_clues,
            scenario_clues=scenario.clues,
            difficulty=scenario.difficulty
        )

        print("XP RESULT:", result_xp)

        if correct:
            message = "You got it!"
        else:
            message = "Not Quite. Try Again!"

        result = {
            "correct": correct,
            "user_answer": user_answer,
            "message": message,
            "answer_xp": result_xp["answer_xp"],
            "clue_xp": result_xp["clue_xp"],
            "total_xp": result_xp["total_xp"],
            "total_score": score["total_score"],
            "difficulty_points": score["difficulty_points"]
        }

        # Find the next scenario
        if scenario.id >= LEVEL_1_END:
            level_complete = True
            next_scenario = None
        else:
         next_scenario = Scenario.query.filter(
            Scenario.id > scenario.id
         ).order_by(
            Scenario.id
         ).first()
         level_complete = False

        print("CURRENT SCENARIO:", scenario.id, scenario.title)

        if next_scenario:
            print("NEXT SCENARIO:", next_scenario.id, next_scenario.title)
        else:
            print("NO MORE SCENARIOS!")

    print("SCENARIO:", scenario)
    print("SCENARIO ID:", scenario.id if scenario else None)
    print("SCENARIO TITLE:", scenario.title if scenario else None)
    print("SCENARIO CONTENT:", scenario.content if scenario else None)

    return render_template(
        "play.html",
        user_answer=user_answer,
        correct=correct,
        scenario=scenario,
        message=message,
        result=result,
        selected_clues=selected_clues,
        level_complete=level_complete,
        next_scenario= next_scenario
    )