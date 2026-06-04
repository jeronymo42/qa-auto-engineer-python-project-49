from brain_games.scripts.game_engine import play_game
from brain_games.scripts.question_even_game import get_even_game_question


def main():
    play_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_even_game_question,
    )


if __name__ == "__main__":
    main()
