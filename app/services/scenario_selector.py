from app.models import Scenario, Attempt
def select_scenario(category, difficulty, user_id):
    attempts = Attempt.query.filter_by(
        user_id=user_id
    ).all()

    attempted_ids = [attempt.scenario_id for attempt in attempts]
    scenarios = Scenario.query.filter(#Used for sqlalchemy expressions like equality etc while filter_by is used for keyword matching
    Scenario.category == category,
    Scenario.difficulty == difficulty,
    Scenario.id.not_in(attempted_ids)
).all()
    return scenarios
