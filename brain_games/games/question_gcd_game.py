from random import randint
from brain_games.games.constants import MIN_NUMBER, MAX_NUMBER


def set_gcd_game_question() -> tuple[str, str]:
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question_text = f"{number1} {number2}"
    number1, number2 = min(number1, number2), max(number2, number1)

    while number2 != 0:
        temp = number2
        number2 = number1 % number2
        number1 = temp

    return question_text, str(number1)
