from brain_games.games.game_engine import play_game
from brain_games.games.question_progression_game import get_progression_game_question


def main():
    play_game(
        "What number is missing in the progression?",
        get_progression_game_question,
    )


if __name__ == "__main__":
    main()
