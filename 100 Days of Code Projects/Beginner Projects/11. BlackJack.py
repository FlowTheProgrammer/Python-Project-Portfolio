"""'
Simple BlackJack Game

Beginner Project: 
There are no try/except
Assume correct inputs

*This project was done after the original blackjack project*
"""

import os
import random
#List of all cards
cards = [11,2,2,3,4,5,6,7,8,9,10,10,10,10]

def getCards(cards):
    hand = []
    for i in range(2):
        hand.append(random.choice(cards))
    return hand

def addCard(player):
    player.append(random.choice(cards))
    return player

def printHands(player,bot):
    print(f"Your cards: {player}")
    print(f"Computer's first card: {bot[0]}")

def printFinalHand(player,bot):
    print(f"Your final hand: {player}")
    print(f"Computer's final hand: {bot}")

def checkWin(player,bot):
    playerscore = 0
    botscore = 0
    numAcesPlayer = player.count(11)

    playerscore = sum(player)
    botscore = sum(bot)
    while True:
        if 11 in player and playerscore > 21 and numAcesPlayer > 0:
            playerscore -= 10
            numAcesPlayer -= 1
        else:
            break

    while True:
        if 11 in bot and botscore > 21:
            botscore -= 10
        else:
            break
    
    if playerscore > botscore and playerscore <= 21:
        return "You Win!"
    elif playerscore == botscore or (botscore > 21 and playerscore > 21):
        return "It's a draw"
    elif (botscore > playerscore and botscore <= 21) or playerscore > 21:
        return "You Lost!"

def botTurn(bot):
    while sum(bot) < 17:
        addCard(bot)
    return bot
    

def startGame():
    os.system("cls")
    user_hand = getCards(cards)
    comp_hand = getCards(cards)
    while True:
        printHands(user_hand,comp_hand)
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            addCard(user_hand)
        elif choice == 'n':
            comp_hand = botTurn(comp_hand)
            printFinalHand(user_hand,comp_hand)
            print(checkWin(user_hand,comp_hand))
            break


while True:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input == "y":
        startGame()
    elif user_input == 'n':
        break
    else:
        os.system("cls")
        print("I don't understand you input\n")
