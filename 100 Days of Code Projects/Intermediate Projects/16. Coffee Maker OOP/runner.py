"""
OOP Version of the Coffee Machine
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from MoneyMaker import MoneyMachine

myMenu = Menu()
moneyMaker = MoneyMachine()
coffee_maker = CoffeeMaker()
while True:
    choices = myMenu.get_items()
    choice = input(f"What would you like to have? {choices}: ")
    choice = choice.lower()
    while choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != 'report' and choice != 'off':
        print("I didn't understand your input, try again!")
        choice = input(f"What would you like to have? {choices}: ")
        choice = choice.lower()
    if choice == "report":
        moneyMaker.report()
        coffee_maker.report()
    elif choice == "off":
        break
    elif myMenu.find_drink(choice):
        my_drink = myMenu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(my_drink):
            if moneyMaker.make_payment(my_drink.cost):
                coffee_maker.make_coffee(my_drink)