from random import randint
from brain_games.games.constants import MIN_NUMBER, MAX_NUMBER


def get_even_game_question() -> tuple[str, str]:
    number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if number % 2 == 0 else "no"
    return str(number), answer
