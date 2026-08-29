from flask import Blueprint, render_template, redirect, url_for, flash, session,request
from forms import RegistrationForm,LoginForm
from app.models import User,Scenario,ScenarioDifficulty,Attempt
from extensions import db
from app.services.calculate_xp import calculate_xp
from app.services.calculate_score import calculate_score

from werkzeug.security import generate_password_hash,check_password_hash
from . import auth_bp,app_bp
user_id = User.query.get(id)

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



@auth_bp.route('/play', methods=['GET','POST'])
def start_training():
    user_answer = None
    correct = None
    message = None
    result = None
    selected_clues = None
    scenario_id = request.form.get("scenario_id")
    scenario = Scenario.query.get(scenario_id) 
    if request.method == "POST": 
     user_answer = request.form.get('answer').lower()#Get the value of user choice either SCAM/LEGIT
     selected_clues = request.form.getlist('clues')#Lists do not have the lower() method
     current_id = request.args.get("next")

     if current_id:
      int_current_id =  int(current_id)
      scenario = Scenario.query.filter(
         Scenario.id > int_current_id
      ).first()
     else:
        scenario = Scenario.query.first()
     print("USER ANSWER: ",user_answer)
     print("CORRECT AnSWER: ",scenario.correct_answer)
     print("SELECTED CLUES: ",selected_clues)
     correct = (user_answer == scenario.correct_answer)#Compare the user's answer and the scenario's correct answer and store the value in correct
     result_xp = calculate_xp(
        correct_answer=correct,
        selected_clues=selected_clues,
        scenario_clues=scenario.clues
     )

     score = calculate_score(
        correct_answer= correct,
        selected_clues=selected_clues,
        scenario_clues=scenario.clues
     )
     print("XP RESULT: ",result_xp)
     if correct:
      message = "You got it!"
     else:
        message = "Not Quite. Try Again!"
     result = {
            "correct": correct,
            "user_answer": user_answer,
            "message": message,
            "answer_xp": result_xp["answer_xp"],#Get the values by indexing the keys
            "clue_xp": result_xp["clue_xp"],
            "total_xp": result_xp["total_xp"],
            "total_score": score['total_score'],
            "difficulty_points": score['difficulty_points']
     }
     attempt = Attempt(
             user_id = user_id,
             scenario_id = scenario_id,
             answer= user_answer,
             correct = result['correct'],
             xp_earned = result_xp['total_xp'],
             score = score['total_score'],
          )

     

    return render_template("play.html", user_answer=user_answer, correct=correct,scenario=scenario, message=message,result=result,selected_clues=selected_clues)
    