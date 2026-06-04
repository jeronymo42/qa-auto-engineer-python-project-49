from brain_games.scripts.game_engine import play_game
from brain_games.scripts.question_calc_game import get_calc_game_question


def main():
    play_game(
        "What is the result of the expression?",
        get_calc_game_question,
    )


if __name__ == "__main__":
    main()
