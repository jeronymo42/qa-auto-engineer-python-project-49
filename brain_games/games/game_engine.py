from collections.abc import Callable

from brain_games.games.constants import NUMBER_OF_GAMES
from brain_games.scripts.cli import get_welcome_user_text
import prompt


def play_game(start_text: str, get_question: Callable[[], tuple[str, str]]) -> None:
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    welcome_text = get_welcome_user_text(user_name)
    print(welcome_text)
    print(start_text)
    games_played = 0
    while games_played < NUMBER_OF_GAMES:
        question_text, correct_answer = get_question()
        print(f"Question: {question_text}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            games_played += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
