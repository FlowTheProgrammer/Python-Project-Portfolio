"""
Simple Calculator
Functions with Returns

Beginner Project: 
There are no try/except
Assume correct inputs
"""

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calc():
    for key in operations:
        print(key)
    
    Running = True

    first_num = float(input("What is the first number?: "))
    while Running:
        symbol = input("Please pick an operation from the lines above: ")
        second_num = float(input("What is the next number?: "))
        which_func = operations[symbol]
        answer = which_func(first_num,second_num)

        print(f"{first_num} {symbol} {second_num} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
            first_num = answer
        else:
            Running = False
            calc()

calc()
