from brain_games.games.game_engine import play_game
from brain_games.games.question_gcd_game import set_gcd_game_question


def main():
    play_game(
        "Find the greatest common divisor of given numbers.",
        set_gcd_game_question,
    )


if __name__ == "__main__":
    main()
