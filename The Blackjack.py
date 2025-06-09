import random
import art
""" random choose card"""
def card_choice():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

""" Define Blackjacks and ace"""
def sum_calculated(c):
    if sum(c) == 21 and len(c):
        return 0
    if sum(c) > 21 and 11 in c:
        c.remove(11)
        c.append(1)

    return sum(c)

""" Define rules of win or lose"""
def win(user_sum, computer_sum):
    if user_sum == computer_sum:
        print('Draw')
    elif user_sum == 0:
        print('Win with a Blackjack!')
    elif computer_sum == 0:
        print('Lose, opponent has Blackjack!')
    elif user_sum > 21:
        print('You went over. You lose!')
    elif computer_sum > 21:
        print('Opponent went over. You win!')
    elif user_sum > computer_sum:
        print('You win!')
    else:
        print('You lose!')

def play_game():
    print(art.logo)
    user = []
    computer = []
    user_score = -1
    computer_score = -1
    game_over = False

    for t in range(2):
        user.append(card_choice())
        computer.append(card_choice())

    while not game_over:
        user_score = sum_calculated(user)
        computer_score = sum_calculated(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            ans = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if ans == 'y':
                user.append(card_choice())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer.append(card_choice())
        computer_score = sum_calculated(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(win(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print('\n'*20)
    play_game()
