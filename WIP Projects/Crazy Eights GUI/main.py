from TwoPlayerCrazyEights import Deck, Hand, Pile
from TwoPlayerCrazyEights import choice,playerView,check_wild,check_deck_count,checkWin
import os

#Game Variables
Playing = True
wild_suit = "" #Tracks the suit of the wild card
start = True #Bool to track the start of a new game

#Init (Sets up deck, discard pile and player hands)
while True:

    #Creates Deck and Discard Pile objects
    newDeck = Deck()
    newDeck.shuffle_deck()
    player_one_hand = Hand()
    player_two_hand = Hand()
    discard_pile = Pile()

    #Deals 5 cards too each player
    for i in range(5):
        player_one_hand.add_card(newDeck.deal_one_card())
        player_two_hand.add_card(newDeck.deal_one_card())
    discard_pile.add_card(newDeck.deal_one_card())
    if discard_pile.cards[-1].rank == "Eight":
        newDeck.reshuffle(discard_pile.return_one_card())
        newDeck.shuffle_deck()
        discard_pile.add_card(newDeck.deal_one_card())
    break

def gameFlow(player):
    global wild_suit
    global Playing
    turn = player
    if player == '1':
        null = input("Player 1's Turn! Press Enter to continue!")
        player = player_one_hand
    elif player == '2':
        null = input("Player 2's turn! Press Enter to continue")
        player = player_two_hand
    os.system('cls')

    #Prints Player View
    playerView(player_one_hand,player_two_hand,discard_pile,turn,wild_suit)

    #Allows player to draw or play
    choice(player,discard_pile,newDeck,wild_suit)

    #Checks if wild card was played in the round
    wild_suit = check_wild(wild_suit,discard_pile)
    null = input("\nPress Enter to end your turn")

    #Checks for win and reshuffle
    Playing = checkWin(player_one_hand,player_two_hand)
    check_deck_count(newDeck,discard_pile)


#Game Logic - Player Turns
while Playing:
    os.system('cls')
    if start:
        print("Welcome to Crazy Eights\n")
        start = False
    gameFlow('1')

    #Game Logic - PLayer 2
    if Playing:
        os.system('cls')
        gameFlow('2')

#Game Logic - Decides winner
os.system("cls")
if player_one_hand.cards == []:
    print("Player1  Won!")
    print("------------")
    if len(player_two_hand.cards) == 1:
        print(f"Player Two had {len(player_two_hand.cards)} card left!")
    else:
        print(f"Player Two had {len(player_two_hand.cards)} cards left!")
elif player_two_hand.cards == []:
    print("Player 2 Won!")
    print("------------")
    if len(player_one_hand.cards) == 1:
        print(f"Player One had {len(player_one_hand.cards)} card left!")
    else:
        print(f"Player One had {len(player_one_hand.cards)} cards left!")