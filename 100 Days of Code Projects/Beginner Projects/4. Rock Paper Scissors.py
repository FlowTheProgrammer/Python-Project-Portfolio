"""
Simple RPS
Lists/Random
Beginner Project: 
There are no try/except
Assume correct inputs
"""
import random

print("Welcome to RPS!")

choices = ["Rock", "Paper","Scissors"]

choice = int(input("Type a number. 0. Rock, 1. Paper or 2. Scissors:\n"))

botChoice = random.randint(0,2)

if choice >= 3 or choice < 0:
    print("No cheating! Invalid input, you lose!")
elif choices[choice] == choices[botChoice]:
    print(f"You both picked {choices[choice]}, it's a draw!")

elif (choice== 0 and botChoice == 2) or (choice == 1 and botChoice == 0) or (choice == 2 and botChoice == 1):
    print(f"The bot chose {choices[botChoice]} and you chose {choices[choice]}. You win!")
    
elif (choice == 0 and botChoice == 1) or (choice == 1 and botChoice == 2) or (choice == 2 and botChoice == 0):
    print(f"The bot chose {choices[botChoice]} and you chose {choices[choice]}. You lose!")