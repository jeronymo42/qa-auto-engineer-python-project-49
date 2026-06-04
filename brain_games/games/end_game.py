def farewell_user(
    user_name: str, user_answer: str | int, correct_answer: str | int
) -> None:
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {user_name}!")
