"""
Simple tip calculator
Simple Arithmetic Python
Beginner Project: 
There are no try/except or loops
Assume correct inputs
"""

print("Tip Calculator!")
bill = int(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

total_bill = bill + (bill*(percentage/100))
split_bill = round(total_bill/split,2)
split_bill = "{:.2f}".format(total_bill/split)

print(f'Each person should pay ${split_bill}')