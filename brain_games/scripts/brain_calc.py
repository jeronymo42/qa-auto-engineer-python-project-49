from brain_games.games.game_engine import play_game
from brain_games.games.question_calc_game import set_calc_game_question


def main():
    play_game(
        "What is the result of the expression?",
        set_calc_game_question,
    )


if __name__ == "__main__":
    main()
