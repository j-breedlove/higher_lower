import random
from os import system

from art import logo, vs
from game_data import data


def format_data(account):
    """ 
    Takes the account data and returns it in a printable format.
    
    Parameters:
    - account (dict): The account details.
    
    Returns:
    - str: Printable format of account details.
    """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """
    Takes the user guess and follower counts and returns if they got it right.
    
    Parameters:
    - user_guess (str): The user's guess ('a' or 'b').
    - a_followers (int): Follower count of account A.
    - b_followers (int): Follower count of account B.
    
    Returns:
    - bool: True if user's guess is correct, False otherwise.
    """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


def main():
    # Display art
    print(logo)
    score = 0
    account_b = random.choice(data)
    game_should_continue = True

    # Game loop
    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers_count = account_a["follower_count"]
        b_followers_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_followers_count, b_followers_count)

        system("clear")
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score is {score}.")
        else:
            print(f"Sorry that's wrong! Final score: {score}")
            game_should_continue = False


if __name__ == "__main__":
    main()
