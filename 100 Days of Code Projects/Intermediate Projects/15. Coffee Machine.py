"""
Coffee Machine
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

def allResources(item):
    allGood = True
    for key in resources:
        if allGood == False:
            break
        if key == "money":
            break
        for i in MENU[item]['ingredients']:
            if i == key:
                if resources[i] >= MENU[item]['ingredients'][i]:
                    allGood = True
                else:
                    allGood = False
                    break
    return allGood

def depleteResource(item):
    for i in MENU:
        if i  == item:
            for x in MENU[item]['ingredients']:
                for y in resources:
                    if x == y:
                        resources[y] = resources[y] - MENU[item]['ingredients'][x]




def coin_Pay(menu,item):
    price = 0
    for i in coinTypes:
        if i != "penny":
            amount = int(input((f"How many {i}s?: "))) * coinTypes[i]
            price += amount
        else:
            amount = int(input(("How many pennies?: ")))
            price += amount

    if price >= menu[item]['cost'] and allResources(item):
        if price > menu[item]['cost']:
            print(f"Purchase Successful! Your change is {round(price - menu[item]['cost'],2)}")
            depleteResource(item)
        else:
            depleteResource(item)
        return True
    elif price >= menu[item]['cost'] and not allResources(item):
        print("Not enough Ingredients! Money Refunded.")
        return False
    elif price < menu[item]['cost'] and allResources(item):
        print("Not enough coins! Money refunded.")
        return False
    elif price < menu[item]['cost'] and not allResources(item):
        print("Insufficient funds and ingedients! Money Refunded.")
        return False

while True:
    user_input = input("What would you like? Espresso/latte/cappuccino?: ")
    user_input = user_input.lower()

    while user_input != "espresso" and user_input != "latte" and user_input != "cappuccino" and user_input != 'report' and user_input != 'off':
        print("I didn't understand your input, try again!")
        user_input = input("What would you like? Espresso/latte/cappuccino?")

    if user_input == "report":
        printReport(resources)
    if user_input == "off":
        break
    elif user_input in MENU:
        if coin_Pay(MENU,user_input):
            resources['money'] = resources['money'] + MENU[user_input]['cost']
            print(f"Here is your {user_input}! ☕")

