from app.models import Scenario, Attempt, ScenarioDifficulty


def select_scenario(category, difficulty, user_id):

    attempts = Attempt.query.filter_by(
        user_id=user_id
    ).all()

    attempted_ids = [
        attempt.scenario_id
        for attempt in attempts
    ]

    difficulty = ScenarioDifficulty(difficulty)

    scenarios = Scenario.query.filter(
        Scenario.category == category,
        Scenario.difficulty == difficulty,
        ~Scenario.id.in_(attempted_ids)
    ).all()

    return scenarios