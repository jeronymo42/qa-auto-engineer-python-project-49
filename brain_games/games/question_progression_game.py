from random import randint
from brain_games.games.constants import (
    MIN_NUMBER,
    MAX_NUMBER,
    MIN_PROGRESSION_LENGTH,
    MAX_PROGRESSION_LENGTH,
    MIN_PROGRESSION_STEP,
    MAX_PROGRESSION_STEP,
)


def get_progression_game_question():
    progression_length = randint(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    step = randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    start_number = randint(MIN_NUMBER, MAX_NUMBER)
    progression = [start_number]
    for i in range(1, progression_length + 1):
        progression.append(progression[i - 1] + step)

    excluded_index = randint(0, progression_length - 1)
    answer = progression[excluded_index]
    progression[excluded_index] = ".."
    question_text = " ".join(map(str, progression))

    return question_text, str(answer)
