from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from forms import RegistrationForm, LoginForm
from app.models import User, Scenario, ScenarioDifficulty, Attempt
from extensions import db, login_manager
from app.services.calculate_xp import calculate_xp
from app.services.calculate_score import calculate_score
from app.services.get_performance import get_performance
from app.services.recommend_training import recommend_training
from app.services.scenario_selector import select_scenario
from sqlalchemy import case
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth_bp, app_bp
from flask_login import login_user, current_user


from app.services.get_performance import get_performance
from app.services.recommend_training import recommend_training
from app.services.ai_engine import ai_recommendation_engine




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app_bp.route('/')
def index():
    return render_template('index.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data.strip().lower()
        password_hash = generate_password_hash(form.password.data)

        if User.query.filter_by(email=email).first():
            flash("This email already exists. Please select a new one.")
            return redirect(url_for('auth_bp.register'))

        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            level=1,
            xp=0
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('auth_bp.login'))

    else:
        print("FORM ERRORS:", form.errors)

    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data.strip().lower()
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, form.password.data):
            session['user'] = user.email
            login_user(user)

            flash('Login successful!', 'success')
            return redirect(url_for('auth_bp.dashboard'))

        flash('Invalid email or password', 'danger')
        return redirect(url_for('auth_bp.login'))

    else:
        print("FORM ERRORS:", form.errors)

    return render_template('login.html', form=form)


@auth_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user = User.query.all()
    return render_template('dashboard.html', user=current_user)


@auth_bp.route('/play', methods=['GET', 'POST'])
def start_training():

    user_answer = None
    correct = None
    message = None
    result = None
    selected_clues = None
    level_complete = False
    next_scenario = None
    performance_result = None
    recommendation = None
    ai_message = None
    LEVEL_1_START = 1
    LEVEL_1_END = 5
    
    LEVEL_2_START = 6
    LEVEL_2_END = 20
    if current_user.level == 1:
        level_start =1
        level_end=5
    else:
        level_start = 6
        level_end =20
    USER_ID = User.query.filter(id=current_user.id)

    performance = get_performance(USER_ID)#Get the actual performance data using the user_id

    print("PERFORMANCE:")
    print(performance)

    recommendation = recommend_training(performance)

    print("\nDETERMINISTIC RECOMMENDATION:")
    print(recommendation)

    ai_message = ai_recommendation_engine(
      performance=performance,
    recommendation=recommendation
    )

    print("\nAI RECOMMENDATION:")
    print(ai_message)

    difficulty_order = case(
        (Scenario.difficulty == ScenarioDifficulty.EASY, 1),
        (Scenario.difficulty == ScenarioDifficulty.MEDIUM, 2),
        (Scenario.difficulty == ScenarioDifficulty.HARD, 3)
    )

    if request.method == "GET":

        next_id = request.args.get("next")

        if next_id:
            scenario = Scenario.query.get(next_id)

        else:
            user_attempts = Attempt.query.filter_by(
                user_id=current_user.id
            ).all()

            attempted_ids = {
                attempt.scenario_id
                for attempt in user_attempts
            }

            if current_user.level == 1:

                scenario = Scenario.query.filter(
                    Scenario.id >= LEVEL_1_START,
                    Scenario.id <= LEVEL_1_END,
                    ~Scenario.id.in_(attempted_ids)
                ).order_by(
                    difficulty_order,
                    Scenario.id
                ).first()

            else:

                performance = get_performance(
                    user_id=current_user.id
                )

                recommendation = recommend_training(
                    performance=performance
                )
                try:
                  ai_message = ai_recommendation_engine(
                  performance=performance,
                  recommendation=recommendation
                )
                except Exception as e:
                  print("AI RECOMMENDATION ERROR:", e)
                  ai_message = "Your training data has been analyzed. Continue practicing to strengthen your scam-detection skills."

                print("AI RECOMMENDATION:", ai_message)

                print(
                    "LEVEL 2 RECOMMENDATION:",
                    recommendation
                )

                focus_categories = recommendation.get(
                    "focus_categories",
                    []
                )

                recommended_difficulty = recommendation.get(
                    "recommended_difficulty",
                    "easy"
                )

                scenario = None

                if focus_categories:

                    scenario = select_scenario(
                        category=focus_categories[0],
                        difficulty=recommended_difficulty,
                        user_id=current_user.id
                    )

                if not scenario:

                    scenario = Scenario.query.filter(
                        Scenario.id >= LEVEL_2_START,
                        Scenario.id <= LEVEL_2_END,
                        ~Scenario.id.in_(attempted_ids)
                    ).order_by(
                        difficulty_order,
                        Scenario.id
                    ).first()

        if not scenario:
            return "No more scenarios available.", 404

    else:

        scenario_id = request.form.get("scenario_id")
        scenario = Scenario.query.get(scenario_id)

        if not scenario:
            return "Scenario not found", 404

        user_answer = request.form.get("answer", "").lower()
        selected_clues = request.form.getlist("clues")

        correct = user_answer == scenario.correct_answer

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

        message = "You got it!" if correct else "Not Quite. Try Again!"

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

        attempt = Attempt(
            answer=user_answer,
            correct=correct,
            score=score["total_score"],
            xp_earned=result_xp["total_xp"],
            user_id=current_user.id,
            scenario_id=scenario.id
        )

        db.session.add(attempt)
        db.session.commit()

        performance = get_performance(
            user_id=current_user.id
        )

        performance_result = {
            "total_attempts": performance["total_attempts"],
            "correct_attempts": performance["correct_attempts"],
            "accuracy": performance["accuracy"],
            "total_score": performance["total_score"],
            "total_xp": performance["total_xp"],
            "category_performance": performance["category_performance"],
            "difficulty_performance": performance["difficulty_performance"]
        }

        if current_user.level == 1:

            if scenario.id == LEVEL_1_END:

                level_complete = True

                recommendation = recommend_training(
                    performance=performance
                )
                try:
                  ai_message = ai_recommendation_engine(
                  performance=performance,
                   recommendation=recommendation
                  )
                except Exception as e:
                  print("AI RECOMMENDATION ERROR:", e)
                  ai_message = "Your training data has been analyzed. Continue practicing to strengthen your scam-detection skills."

                print("AI RECOMMENDATION:", ai_message)

                print(
                    "TRAINING RECOMMENDATION:",
                    recommendation
                )

                focus_categories = recommendation.get(
                    "focus_categories",
                    []
                )

                recommended_difficulty = recommendation.get(
                    "recommended_difficulty",
                    "easy"
                )

                if focus_categories:

                    next_scenario = select_scenario(
                        category=focus_categories[0],
                        difficulty=recommended_difficulty,
                        user_id=current_user.id
                    )

                    print(
                        "LEVEL 2 PREVIEW SCENARIO:",
                        next_scenario
                    )

            else:

                next_scenario = Scenario.query.filter(
                    Scenario.id > scenario.id,
                    Scenario.id <= LEVEL_1_END
                ).order_by(
                    Scenario.id
                ).first()

        else:

            recommendation = recommend_training(
                performance=performance
            )

            print(
                "LEVEL 2 RECOMMENDATION:",
                recommendation
            )

            focus_categories = recommendation.get(
                "focus_categories",
                []
            )

            recommended_difficulty = recommendation.get(
                "recommended_difficulty",
                "easy"
            )

            if focus_categories:

                next_scenario = select_scenario(
                    category=focus_categories[0],
                    difficulty=recommended_difficulty,
                    user_id=current_user.id
                )

            if not next_scenario:

                attempted_ids = {
                    attempt.scenario_id
                    for attempt in Attempt.query.filter_by(
                        user_id=current_user.id
                    ).all()
                }

                next_scenario = Scenario.query.filter(
                    Scenario.id >= LEVEL_2_START,
                    Scenario.id <= LEVEL_2_END,
                    ~Scenario.id.in_(attempted_ids)
                ).order_by(
                    difficulty_order,
                    Scenario.id
                ).first()

        print(
            "CURRENT SCENARIO:",
            scenario.id,
            scenario.title
        )

        if next_scenario:
            print(
                "NEXT SCENARIO:",
                next_scenario.id,
                next_scenario.title
            )
        else:
            print("NO MORE SCENARIOS!")

    return render_template(
        "play.html",
        user_answer=user_answer,
        correct=correct,
        scenario=scenario,
        message=message,
        result=result,
        selected_clues=selected_clues,
        level_complete=level_complete,
        next_scenario=next_scenario,
        performance_result=performance_result,
        recommendation=recommendation,
        ai_message=ai_message
    )


@auth_bp.route('/next-level')
def next_level():

    if current_user.level >= 2:
        return redirect(url_for('auth_bp.start_training'))

    current_user.level = 2
    db.session.commit()

    flash('Level 2 unlocked!', 'success')

    return redirect(url_for('auth_bp.start_training'))