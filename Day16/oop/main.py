from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

print(logo)

myMachine = CoffeeMaker()
myMoneyMachine = MoneyMachine()
myMenu = Menu()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
is_machine_on = True

while is_machine_on:

    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        # TODO: 3. Print report.
        myMachine.report()
        myMoneyMachine.report()
    else:
        drink = myMenu.find_drink(choice)

        if myMachine.is_resource_sufficient(drink):
            if myMoneyMachine.make_payment(drink.cost):
                myMachine.make_coffee(drink)


