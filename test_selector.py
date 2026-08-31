from app import create_app
from app.services.scenario_selector import select_scenario


app = create_app()

with app.app_context():

    USER_ID = 6

    scenario = select_scenario(
        category="phishing",
        difficulty="hard",
        user_id=USER_ID
    )

    print("\nSELECTED SCENARIO:")

    if scenario:
        print(
            scenario.id,
            scenario.title,
            scenario.category,
            scenario.difficulty.value
        )
    else:
        print("No matching scenario found.")