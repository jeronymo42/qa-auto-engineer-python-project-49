from brain_games.games.game_engine import play_game
from brain_games.games.question_even_game import set_even_game_question


def main():
    play_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        set_even_game_question,
    )


if __name__ == "__main__":
    main()
