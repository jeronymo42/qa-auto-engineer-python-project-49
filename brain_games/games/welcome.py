from brain_games.scripts.cli import welcome_user
import prompt


def welcome() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    welcome_text = welcome_user(name)
    print(welcome_text)
    return name
