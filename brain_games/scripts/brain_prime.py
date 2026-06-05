from brain_games.games.game_engine import play_game
from brain_games.games.question_prime_game import get_prime_game_question


def main():
    play_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        get_prime_game_question,
    )


if __name__ == "__main__":
    main()
