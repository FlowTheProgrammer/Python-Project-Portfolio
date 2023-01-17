"""
Coffee Machine

Not-Finished
"""

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
    "money": 0,
}

coinTypes = {
    "quarter": .25,
    "dime": .10,
    "nickel": .05,
    "penny": .01
}

def printReport(res):
    print(f"Water: {res['water']}")
    print(f"Milk: {res['milk']}")
    print(f"Coffee: {res['coffee']}")
    print(f"Money: {res['money']}")

def coin_Pay(menu,item):
    price = 0
    for i in coinTypes:
        if i != "penny":
            amount = int(input((f"How many {i}s?: ")))
            price += amount
        else:
            amount = int(input(("How many pennies?: ")))
            price += amount

    ig 
    
    return True

 

user_input = input("What would you like? Espresso/latte/cappuccino?: ")

while user_input != "espresso" and user_input != "latte" and user_input != "cappuccino" and user_input != 'report':
    print("I didn't understand your input, try again!")
    user_input = input("What would you like? Espresso/latte/cappuccino?")

if user_input.lower() == "report":
    printReport(resources)
elif user_input.lower() in MENU:
    if coin_Pay(MENU,user_input):
        print("Yay!")

