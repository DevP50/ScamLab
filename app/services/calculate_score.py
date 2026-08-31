from app.models import ScenarioDifficulty


def calculate_score(
    correct_answer,
    difficulty,
    scenario_clues,
    selected_clues
):

    if not correct_answer:
        return {
            "total_score": 0,
            "answer_xp": 0,
            "clue_xp": 0,
            "wrong_clue_xp": 0,
            "difficulty_points": 0
        }

    answer_points = 50

    correct_clues = sum(
        1
        for clue in selected_clues
        if clue in scenario_clues
    )

    wrong_clues = sum(
        1
        for clue in selected_clues
        if clue not in scenario_clues
    )

    clue_points = correct_clues * 10
    wrong_clue_penalty = wrong_clues * 5

    if difficulty == ScenarioDifficulty.EASY:
        difficulty_points = 0

    elif difficulty == ScenarioDifficulty.MEDIUM:
        difficulty_points = 5

    elif difficulty == ScenarioDifficulty.HARD:
        difficulty_points = 10

    else:
        difficulty_points = 0

    total_score = (
        answer_points
        + clue_points
        - wrong_clue_penalty
        + difficulty_points
    )

    return {
        "total_score": total_score,
        "answer_xp": answer_points,
        "clue_xp": clue_points,
        "wrong_clue_xp": wrong_clue_penalty,
        "difficulty_points": difficulty_points
    }