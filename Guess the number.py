import random
logo=("""
        _____                   __  __                         __             __
        / ___/_ _____ ___ ___   / /_/ /  ___   ___  __ ____ _  / /  ___ ____  / /
        / (_ / // / -_|_-<(_-<  / __/ _ \/ -_) / _ \/ // /  ' \/ _ \/ -_) __/ /_/
        \___/\_,_/\__/___/___/  \__/_//_/\__/ /_//_/\_,_/_/_/_/_.__/\__/_/   (_)
                                                                         """)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def time():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
        return 10
    else:
        return 5


def check_answer(guess, c_guess, times):
    if guess < c_guess:
        print('Too low. \nGuess again.')
        return times-1
    elif guess > c_guess:
        print('Too high. \nGuess again.')
        return times-1
    else:
        print(f'You got it!The answer was {c_guess}.')
        return times


def game():
    times = time()

    guess = 0
    c_guess = random.randint(1, 100)

    while times > 0:
        print(f'You have {times} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        times = check_answer(guess, c_guess, times)

        if guess == c_guess:
            break
        elif times == 0:
            print(f'Game Over. You lose! The correct number was {c_guess}.')

game()

# is_correct=False
# while not is_correct:
#     if guess < c_guess:
#         print('Too low. \nGuess again.')
#         guess = int(input('Make a guess: '))
#         print(f'You have {times-1} attempts remaining to guess the number.')
#     elif guess > c_guess:
#         print('Too high. \nGuess again.')
#         guess = int(input('Make a guess: '))
#         print(f'You have {times-1} attempts remaining to guess the number.')
#     else:
#         print(f'You got it!The answer was {guess}.')
#         is_correct=True
#
#     if times == 0:
#         print('Game Over. You lose!')
#         is_correct=True
