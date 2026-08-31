from app.services.ai_engine import ai_recommendation_engine


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
    },

    "difficulty_performance": {
        "easy": {
            "attempts": 4,
            "correct": 3,
            "accuracy": 75
        },
        "medium": {
            "attempts": 4,
            "correct": 2,
            "accuracy": 50
        },
        "hard": {
            "attempts": 2,
            "correct": 1,
            "accuracy": 50
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
    performance=performance,
    recommendation=recommendation
)

print("\nAI RECOMMENDATION:")
print(result)