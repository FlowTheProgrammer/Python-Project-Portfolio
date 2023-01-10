"""
Hangman game
Loops/List/If-statements

Used some advanced functions for simplicity
"""
from random_word import RandomWords

r = RandomWords()

randomWord = r.get_random_word()

wordList = []

for i in range(len(randomWord)):
    wordList.append("_")

Playing = True
Lives = 6

print("Welcome to Hangman!")

while Playing:
    guess_letter = input("\nGuess a letter: ").lower()

    if guess_letter in wordList:
        print("You already guessed that letter!\n")

    for i,letter in enumerate(randomWord):
        if guess_letter == letter:
            wordList[i] = guess_letter

    if guess_letter not in randomWord:
        Lives -= 1
        print(f"\nLetter not in word. Lives:{Lives}\n")
        if Lives == 0:
            Playing = False
            print("You Lost!")
            print(f'\nThe word was {randomWord}')

    print(wordList)
    if "_" not in wordList:
        Playing = False
        print("You have won!")