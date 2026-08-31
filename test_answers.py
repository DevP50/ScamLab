from app import create_app
from app.models import Scenario

app = create_app()

with app.app_context():

    scenarios = Scenario.query.filter(
        Scenario.id.in_([1, 2, 3, 4, 5])
    ).all()

    for scenario in scenarios:
        print(
            scenario.id,
            "| TITLE:", scenario.title,
            "| CORRECT ANSWER:", repr(scenario.correct_answer)
        )