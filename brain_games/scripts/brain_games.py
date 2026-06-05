import prompt
from brain_games.scripts.cli import get_welcome_user_text


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(get_welcome_user_text(name))


if __name__ == "__main__":
    main()
