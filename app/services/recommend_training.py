def recommend_training(performance):

    category_performance = performance["category_performance"]
    difficulty_performance = performance["difficulty_performance"]
    #Original Gamestate the player has not attempted any scenarios yet
    if not category_performance:
        return {
            "primary_weakness": None,
            "recommended_difficulty": "easy",
            "focus_categories": [],
            "reason": "Not enough performance data yet."
        }

    # Find the weakest category
    weakest_category = min(
        category_performance,
        key=lambda category : category_performance[category]["accuracy"]
    )

    weakest_accuracy = category_performance[
        weakest_category
    ]["accuracy"]

    # Decide difficulty
    if weakest_accuracy < 50:
        recommended_difficulty = "easy"

    elif weakest_accuracy < 75:
        recommended_difficulty = "medium"

    else:
        recommended_difficulty = "hard"

    return {
        "primary_weakness": weakest_category,
        "recommended_difficulty": recommended_difficulty,
        "focus_categories": [weakest_category],
        "reason": (
            f"The user is weakest in {weakest_category} "
            f"with {weakest_accuracy}% accuracy."
        )
    }