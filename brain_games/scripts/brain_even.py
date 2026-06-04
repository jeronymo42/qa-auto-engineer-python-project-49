from brain_games.scripts.welcome import welcome
from brain_games.scripts.constants import NUMBER_OF_GAMES, MIN_NUMBER, MAX_NUMBER
from brain_games.scripts.end_game import farewell_user
import prompt
from random import randint


def main():
    user_name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    games_played = 0
    while games_played < NUMBER_OF_GAMES:
        number = randint(MIN_NUMBER, MAX_NUMBER)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if (answer == "no" and number % 2) or (answer == "yes" and number % 2 == 0):
            print("Correct!")
            games_played += 1
        else:
            farewell_user(user_name, answer, 'no' if number % 2 else 'yes')
            return
    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
