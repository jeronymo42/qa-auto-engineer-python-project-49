from random import randint
from brain_games.scripts.constants import MIN_NUMBER, MAX_NUMBER


def get_even_game_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if number % 2 == 0 else "no"
    return number, answer
