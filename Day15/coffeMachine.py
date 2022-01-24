from art import logo


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_drink(a_drink, menu_drink):
    if a_drink['water'] > menu_drink['water']:
        return "Sorry there is not enough water."
    elif a_drink['milk'] > menu_drink['milk']:
        return "Sorry there is not enough milk."
    elif a_drink['coffee'] > menu_drink['coffee']:
        return "Sorry there is not enough coffee."


print(logo)

money = 0

active = True

print(MENU['latte'])

while active:

    request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 1: print Report
    if request == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")

    # TODO: 2: Check resources sufficient
    else:
        drink = MENU(request)

        print(drink)

        check_drink(drink, resources)

