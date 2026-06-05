from random import randint, choice
from brain_games.games.constants import MIN_NUMBER, MAX_NUMBER, MATH_OPERATIONS


def get_calc_game_question() -> tuple[str, str]:
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    math_function = choice(MATH_OPERATIONS)
    question = f"{number1} {math_function} {number2}"
    answer = str(eval(question))
    return question, answer
