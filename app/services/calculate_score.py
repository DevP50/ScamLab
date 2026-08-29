def calculate_score(correct_answer,difficulty,scenario_clues,selected_clues):
    answer_xp = 0
    wrong_clue_xp = 0
    correct_clue_points = 0
    wrong_clue_points = 0
    difficulty_points = 0
    if correct_answer:
        answer_xp = 50
        for clue in selected_clues:
           if clue in scenario_clues:
            correct_clue_points += 1
            clue_xp = correct_clue_points * 10
           else:
            wrong_clue_points += 1
            wrong_clue_xp = wrong_clue_points * 5
            if difficulty == "EASY":
               difficulty_points += 0
            elif difficulty == "MEDIUM":
               difficulty_points += 5
            elif difficulty == "HARD":
               difficulty_points += 10
    total_score = clue_xp + answer_xp - wrong_clue_xp + difficulty_points

    return {
       "total_score": total_score,
       "answer_xp": answer_xp,
       "clue_xp": clue_xp,
       "wrong_clue_xp": wrong_clue_xp,
       "difficulty_points": difficulty_points
    }

    
