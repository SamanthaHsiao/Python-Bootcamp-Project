import game_data
import art
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

Final_score = 0
correct = True

while correct:
    A = random.choice(game_data.data)
    B = random.choice(game_data.data)
    if A == B:
        B = random.choice(game_data.data)

    print(art.logo)
    print(f"Compare A: {format_data(A)}.")
    print(art.vs)
    print(f"Against B: {format_data(B)}.")

    choice = input(f"Who has more followers? Type 'A' or 'B': ").upper()

    a_count = A["follower_count"]
    b_count = B["follower_count"]

    if choice == 'A':
        if a_count > b_count:
            Final_score += 1
            print(f"You're right! Current score: {Final_score}\n")
        else:
            print(f"Sorry, that's wrong. Final score: {Final_score}")
            correct = False
    elif choice == 'B':
        if b_count > a_count:
            Final_score += 1
            print(f"You're right! Current score: {Final_score}\n")
        else:
            print(f"Sorry, that's wrong. Final score: {Final_score}")
            correct = False

# Other Solution
# def check_answer(user_guess, a_followers, b_followers):
#     """Take a user's guess and the follower counts and returns if they got it right."""
#     if a_followers > b_followers:
#         return user_guess == "a"
#     else:
#         return user_guess == "b"
