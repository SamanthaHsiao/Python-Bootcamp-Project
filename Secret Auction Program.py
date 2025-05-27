# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def find_highest_bidder(price):

    winner = ''
    winner_price = 0

    for name, value in price.items():
        if int(value) > winner_price:
            winner = name
            winner_price = int(value)

    print(f"The winner is {winner} with a bid of ${winner_price}. ")

price = {}
should_continue = True
while should_continue:
    name = input("What is your name?")
    bid = input("What is your bid? $")
    price[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if other == 'no':
        should_continue = False
        find_highest_bidder(price)
    elif other == 'yes':
        print("\n" * 20)
