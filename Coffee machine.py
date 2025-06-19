MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Todo1 Check the user’s input to decide what to do next.  &Print report.
def report_resource():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"


#Todo2 Check resources sufficient &Process coins.
# c_water = MENU[choice]['ingredients']['water']
# c_milk = MENU[choice]['ingredients']['milk']
# c_coffee = MENU[choice]['ingredients']['coffee']
# r_water = resources['water']
# r_milk = resources['milk']
# r_coffee = resources['coffee']
def is_sufficient(customer_coffee):
    for item in customer_coffee:
        if resources[item] < customer_coffee[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def cost():
    pay = 0
    print("Please insert coin.")
    pay += int(input("how many quarters?:"))*0.25
    pay += int(input("how many dimes?:"))*0.1
    pay += int(input("how many nickles?:"))*0.05
    pay += int(input("how many pennies?:"))*0.01
    return pay

#Todo3 Check transaction successful?
def is_transaction_successful(received, coffee_price):
    if coffee_price > received:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += coffee_price
        change = round((received - coffee_price), 2)
        print(f"Here is ${change} in change.")
        return True

#Todo4 Make Coffee
def make_coffee(coffee, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee}. Enjoy!")

get_coffee = True
while get_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        get_coffee = False
    else:
        if choice == 'report':
            print(f"{report_resource()}\nMoney: {profit}")
        else:
            drink = MENU[choice]
            if is_sufficient(drink['ingredients']):
                if is_transaction_successful(cost(), drink['cost']):
                    make_coffee(choice, drink['ingredients'])

# feedback:
# First time I right can't repeat.
# Practice to use def() to complete. Reduce the complication of code. def() can do by true/ false
# Use global statement profit in local def()
