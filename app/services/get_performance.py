from app.models import Attempt


def get_performance(user_id):
#Gets all the  attempts for a specific user 
    attempts = Attempt.query.filter_by(
        user_id=user_id
    ).all()

    if not attempts:
        return {
            "total_attempts": 0,
            "correct_attempts": 0,
            "accuracy": 0,
            "total_score": 0,
            "total_xp": 0,
            "category_performance": {},
            "difficulty_performance": {}
        }

    total_attempts = len(attempts)
    correct_attempts = sum(1 for attempt in attempts if attempt.correct)

    accuracy = round(
        (correct_attempts / total_attempts) * 100,
        2
    )

    total_score = sum(attempt.score for attempt in attempts)
    total_xp = sum(attempt.xp_earned for attempt in attempts)

    category_performance = {}
    difficulty_performance = {}

    for attempt in attempts:

        scenario = attempt.user_scenario

        if not scenario:
            continue

        category = scenario.category
        difficulty = scenario.difficulty.value

        # CATEGORY
        if category not in category_performance:
            category_performance[category] = {
                "attempts": 0,
                "correct": 0,
                "accuracy": 0
            }

        category_performance[category]["attempts"] += 1

        if attempt.correct:
            category_performance[category]["correct"] += 1

        category_performance[category]["accuracy"] = round(
            (
                category_performance[category]["correct"]
                /
                category_performance[category]["attempts"]
            ) * 100,
            2
        )

        # DIFFICULTY
        if difficulty not in difficulty_performance:
            difficulty_performance[difficulty] = {
                "attempts": 0,
                "correct": 0,
                "accuracy": 0
            }

        difficulty_performance[difficulty]["attempts"] += 1

        if attempt.correct:
            difficulty_performance[difficulty]["correct"] += 1

        difficulty_performance[difficulty]["accuracy"] = round(
            (
                difficulty_performance[difficulty]["correct"]
                /
                difficulty_performance[difficulty]["attempts"]
            ) * 100,
            2
        )

    return {
        "total_attempts": total_attempts,
        "correct_attempts": correct_attempts,
        "accuracy": accuracy,
        "total_score": total_score,
        "total_xp": total_xp,
        "category_performance": category_performance,
        "difficulty_performance": difficulty_performance
    }