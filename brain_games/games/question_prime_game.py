from random import randint
from brain_games.games.constants import MIN_NUMBER, MAX_NUMBER


def check_prime(number):
    if number < 4:
        return True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_prime_game_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = "yes" if check_prime(number) else "no"
    return number, answer
