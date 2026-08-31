from app import create_app
from app.models import User, Attempt
from app.services.get_performance import get_performance
from app.services.recommend_training import recommend_training
from app.services.scenario_selector import select_scenario

app = create_app()

with app.app_context():

    users = User.query.all()

    for user in users:

        performance = get_performance(user.id)

        if performance["total_attempts"] < 5:
            continue

        recommendation = recommend_training(performance)

        category = recommendation.get("primary_weakness")
        difficulty = recommendation.get("recommended_difficulty")

        if not category:
            continue

        matching_scenario = select_scenario(
            category=category,
            difficulty=difficulty,
            user_id=user.id
        )

        if matching_scenario:

            print("\n==============================")
            print("LEVEL 2 TEST USER FOUND")
            print("==============================")
            print("USER ID:", user.id)
            print("USERNAME:", user.username)

            print("\nPERFORMANCE:")
            print(performance)

            print("\nRECOMMENDATION:")
            print(recommendation)

            print("\nMATCHING SCENARIO:")
            print(
                matching_scenario.id,
                matching_scenario.title,
                matching_scenario.category,
                matching_scenario.difficulty.value
            )

            break

    else:
        print("No suitable Level 2 test user found.")