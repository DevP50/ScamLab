def calculate_xp(correct_answer, selected_clues, scenario_clues):

    answer_xp = 50 if correct_answer else 0

    correct_clues = sum(
        1
        for clue in selected_clues
        if clue in scenario_clues
    )

    clue_xp = correct_clues * 10 if correct_answer else 0

    total_xp = answer_xp + clue_xp

    return {
        "answer_xp": answer_xp,
        "clue_xp": clue_xp,
        "total_xp": total_xp
    }