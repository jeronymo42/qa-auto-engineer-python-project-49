from collections.abc import Callable

from brain_games.games.welcome import welcome
from brain_games.games.constants import NUMBER_OF_GAMES
from brain_games.games.end_game import farewell_user
import prompt


def play_game(start_text: str, get_question: Callable[[], tuple[str, str]]) -> None:
    user_name = welcome()
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
            farewell_user(user_name, user_answer, correct_answer)
            return
    print(f"Congratulations, {user_name}!")
