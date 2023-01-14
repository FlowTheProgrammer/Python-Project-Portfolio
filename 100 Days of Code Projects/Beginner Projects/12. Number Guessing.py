"""'
Simple Number Guessing Game
Scope

Beginner Project: 
There are no try/except
Assume correct inputs
"""

import random
print("Welcome  to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

lives = 0
number = random.randint(1,100)

while True:
    diff = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
    if diff.lower() == 'easy':
        lives = 10
        break
    elif diff.lower() == "hard":
        lives = 5
        break
    else:
        print("I dont understand. Try Again.")

while lives != 0:
    print(f"Attempts Remaining: {lives}")
    guess = int(input("Guess a number: "))
    if guess != number and guess > number:
        print("Too High!")
        lives-=1
    elif guess != number and guess < number:
        print("Too Low!")
        lives-=1
    else:
        break

if lives != 0:
    print("You Win!")
else:
    print("You ran out of guesses, you lose!")

