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


def coins_cal(quarters, dimes, nickles, pennies):
    return (0.25*quarters)+(dimes*.10)+(nickles*.5)+(.01* pennies)


print(logo)

money = 0

active = True

# print(resources)


def coffee():
    global money
    while active:

        request = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 1: print Report
        if request == 'report':
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
            coffee()

        drink = MENU[request]['ingredients']

        # TODO: 2: Check resources sufficient
        if drink['water'] > resources['water']:
             print("Sorry there is not enough water.")
             coffee()
        elif drink['milk'] > resources['milk']:
            print("Sorry there is not enough milk.")
            coffee()
        elif drink['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
            coffee()
        else:
            print("Please insert coins.")
            quarter = int(input("How many quarter?: "))
            dime = int(input("How many dime?: "))
            nickle = int(input("How many nickle?: "))
            pennie = int(input("How many penny?: "))

            cash = coins_cal(quarter, dime, nickle, pennie)

            cost = MENU[request]['cost']

            if cost > cash:
                print("Sorry that's not enough money. Money refunded.")
                coffee()
            else:
                change = cash - cost
                print(f"Here is ${change} in change.")
                print(f"Here is you {request} Enjoy!")
                money += cost
                resources['water'] -= drink['water']
                resources['milk'] -= drink['milk']
                resources['coffee'] -= drink['coffee']





coffee()
