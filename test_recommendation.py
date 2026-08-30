from app.services.recommend_training import recommend_training

performance = {
    "category_performance": {
        "impersonation": {
            "attempts": 5,
            "correct": 2,
            "accuracy": 40
        },
        "phishing": {
            "attempts": 5,
            "correct": 5,
            "accuracy": 100
        },
        "mobile_money": {
            "attempts": 5,
            "correct": 4,
            "accuracy": 80
        }
    },
    "difficulty_performance": {}
}

recommendation = recommend_training(performance)

print(recommendation)