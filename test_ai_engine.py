def ai_recommendation_engine(performance, recommendation):

    category_performance = performance["category_performance"]
    primary_weakness = recommendation["primary_weakness"]
    recommended_difficulty = recommendation["recommended_difficulty"]
    reason = recommendation["reason"]

    return {
        "focus_category": primary_weakness,
        "recommended_difficulty": recommended_difficulty,
        "reason": reason,
        "category_performance": category_performance
    }


performance = {
    "category_performance": {
        "impersonation": {
            "attempts": 5,
            "correct": 2,
            "accuracy": 40
        },
        "phishing": {
            "attempts": 5,
            "correct": 4,
            "accuracy": 80
        }
    }
}

recommendation = {
    "primary_weakness": "impersonation",
    "recommended_difficulty": "easy",
    "focus_categories": ["impersonation"],
    "reason": "The user is weakest in impersonation with 40% accuracy."
}


result = ai_recommendation_engine(
    performance,
    recommendation
)

print(result)