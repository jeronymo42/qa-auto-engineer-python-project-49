import prompt
from brain_games.scripts.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(welcome_user(name))


if __name__ == "__main__":
    main()
