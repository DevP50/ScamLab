def ai_recommandtion_engine(performance,recommendation):
    category_performance = performance['category_performance']
    primary_weakness = recommendation['primary_weakness']
    recommended_difficulty = recommendation['recommend_difficulty']
    reason = recommendation['reason']

    return {
        "focus_category": primary_weakness,
        "recommended_difficulty": recommended_difficulty,
        "reason": reason,
        "category_performance": category_performance
    }