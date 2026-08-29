def calculate_xp(correct_answer,selected_clues,scenario_clues):
     answer_xp = 0
     clue_xp = 0
     if correct_answer:
         answer_xp = 50 
         wrong_selected_clues = 0
         correct_selected_clues = 0

         for clue in selected_clues:
           if clue in scenario_clues:
            correct_selected_clues += 1
           else:
              wrong_selected_clues += 1
         clue_xp = correct_selected_clues * 10

     total_xp = answer_xp + clue_xp

     return {
        "answer_xp": answer_xp,
        "clue_xp": clue_xp,
        "total_xp": total_xp
    }

