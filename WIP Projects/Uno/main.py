"""
UNO

House Rules:

Player can either pick up one card or play a card
A player doesn't need to draw until they get a useable card
No Stacking colors or +2's
Winner is determined by the first person to get rid of all their cards
"""

from Uno import Deck, Hand, Pile
from Uno import choice,playerView,check_wild,check_deck_count,checkWin,skipPlayer,reversePlayer,drawCards
import os

#Game Variables
Playing = True
wild_suit = "" #Tracks the suit of the wild card
start = True #Bool to track the start of a new game
players = []
cant_start = ['Wild','Reverse','Skip',"+2",'+4']
winner = ''

#Player who is playing
who_is_playing = 1
direction = 1

#ADD ERROR CHECKING
while True:
    try:
        amt = int(input("How many players will be playing?: "))
        if amt > 1 and amt <= 10:
            break
        else:
            os.system('cls')
            null = input("Enter a number from 2-10. Press Enter to Continue")
            os.system('cls')
    except:
        os.system('cls')
        null = input("Please input a number. Press Enter to Continue.")
        os.system('cls')


#Creates Deck and Discard Pile objects
newDeck = Deck()
newDeck.shuffle_deck()
discard_pile = Pile()

#Deals 7 cards to each player
for pos in range(amt):
    thisHand = Hand()
    for i in range(7):
        thisHand.add_card(newDeck.deal_one_card())
    players.append([str(pos + 1),thisHand])
    discard_pile.add_card(newDeck.deal_one_card())

#Loops until starting card isn't a power card
while discard_pile.cards[-1].rank in cant_start:
    newDeck.reshuffle(discard_pile.return_one_card())
    newDeck.shuffle_deck()
    discard_pile.add_card(newDeck.deal_one_card())


def gameFlow(player):
    """Funciton to simulate Game Flow"""

    global wild_suit
    global Playing

    #Prompts User
    null = input(f"Player {player[0]}'s Turn! Press Enter to continue!")
    position = player[0]
    player_hand = player[1]
    os.system('cls')

    #Prints Player View
    playerView(position,player_hand,players,discard_pile,wild_suit)

    #Allows player to draw or play
    choice(position,player_hand,discard_pile,newDeck,wild_suit)

    #Checks if wild card was played in the round
    wild_suit = check_wild(wild_suit,discard_pile)
    null = input("\nPress Enter to end your turn")

    #Checks for win and reshuffle
    Playing = checkWin(players)
    check_deck_count(newDeck,discard_pile)

    return (skipPlayer(),reversePlayer())

def gamePenalty(type):
    
    pass

def checkPlaying():
    global who_is_playing

    #Used to handle skips and reverse
    if who_is_playing == len(players) + 2: #Handles in only rwo players are playing
        who_is_playing = 2 
    elif who_is_playing > len(players):
        who_is_playing = 1
    elif who_is_playing < 1:
        who_is_playing = len(players)


#Game Logic - Player Turns


while Playing:

    player = players[who_is_playing - 1]

    if Playing: 
        os.system('cls')
        if start:
            print("Uno Game!\n")
            start = False
        skipped,reversed = gameFlow(player)
        winner = player[0] #To keep track of turn: If end on this turn, thefore winner

        if skipped:
            who_is_playing += (2 * direction)
            checkPlaying()
            gamePenalty('skipped')

        elif reversed:
            if len(players) == 2:
                who_is_playing += (2 * direction) #Skips player instead if only 2 players
                checkPlaying()
                gamePenalty('skipped')
            else:
                direction *= -1
                who_is_playing += (1 * direction)
                checkPlaying()
                gamePenalty('reversed')

        else:
            who_is_playing += (1 * direction)
            checkPlaying()


#Game Logic - Decides winner
os.system("cls")
print(f"Player {winner} Won!")
print("-------------")
