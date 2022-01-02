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

# resource checker

def rChecker(coffee_name):
    print(f"Coffe type: {coffee_name}\nIngredients: {MENU[coffee_name]['ingredients']}\nPrice: ${MENU[coffee_name]['cost']} ")
    drink = MENU[coffee_name]['ingredients']
    items = len(MENU[coffee_name]['ingredients'])

    if drink["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            coffee()
    elif drink['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
            coffee()
    elif items == 3:
        if drink['milk'] > resources['milk']:
            print("Sorry there is not enough milk.")
            coffee()


# deduct resources after making the coffee
def dResource(coffee_name):
    drink = MENU[coffee_name]['ingredients']
    items = len(MENU[coffee_name]['ingredients'])

    resources['water'] -= drink['water']
    resources['coffee'] -= drink['coffee']

    if items == 3:
        resources['milk'] -= drink['milk']


def coffee():
    global money, active
    while active:

        request = input("What would you like? (espresso/latte/cappuccino): ").lower()


        if request == 'off':
            active = False
            exit(0)

        # TODO: 1: print Report
        elif request == 'report':
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
            coffee()

        drink = MENU[request]['ingredients']

        # TODO: 2: Check resources sufficient

        # check to see if there is sufficient amount of resources
        rChecker(request)

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
            change = round((cash - cost), 2)
            print(f"Here is ${change} in change.")
            print(f"Here is you {request} Enjoy!")
            money += cost

            dResource(request)


coffee()
