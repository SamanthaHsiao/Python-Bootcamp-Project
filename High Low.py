import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score=0
    # print(f"The computer's number is {cnum}")
    
    for i in range(0, NUM_ROUNDS):
        cnum=random.randint(1, 100)
        mnum=random.randint(1, 100)
        print(f"Round {i+1}")
        print(f"Your number is {mnum}")   
        ans=input("Do you think your number is higher or lower than the computer's?: ")
        if cnum > mnum:
            if ans == "lower":
                print(f"You were right! The computer's number was {cnum}")
                score += 1
            else:
                print(f"Aww, that's incorrect. The computer's number was {cnum}")
        elif cnum < mnum:
            if ans == "higher":
                print(f"You were right! The computer's number was {cnum}")
                score += 1
            else:
                print(f"Aww, that's incorrect. The computer's number was {cnum}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {cnum}")
        print(f"Your score is now {score}\n")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
