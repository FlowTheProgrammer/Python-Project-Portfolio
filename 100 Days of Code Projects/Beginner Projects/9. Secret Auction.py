"""
Secret Auction 
Dicts

Beginner Project: 
There are no try/except
Assume correct inputs
"""

import os
bids = {}
print("Welcome to the Secret Auciton")

while True:
    user_input = input("What is your name?")
    bid = int(input("What is your bid?: $"))

    bids[user_input] = bid
    cont = input("Are there more bidders? Yes or No.")

    if cont.lower() == "yes":
        os.system("cls")
        pass
    elif cont.lower() == "no":
        os.system("cls")
        break

max_num = 0
person = ''
for people in bids:
    bid_amount = bids[people]
    if bid_amount > max_num:
        max_num = bid_amount
        person = people

print(f"The winner is {person} with a bid of ${max_num}!")