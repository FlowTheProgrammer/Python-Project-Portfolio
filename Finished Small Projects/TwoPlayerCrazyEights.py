"""
Simple Crazy Eights-like game

House Rules:

Player can either pick up one card or play a card
A player doesn't need to draw until they get a useable card
Winner is determined by the first person to get rid of all their cards
"""

import random
import os

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 

#Card Class - Creates Cards
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__ (self):
        return f'{self.rank} of {self.suit}'

#Deck Class - Creates 52 Card Objects
class Deck():

    def __init__(self):

        self.allCards = []

        for suit in suits:
            for rank in ranks:
                added_card = Card(suit,rank)
                self.allCards.append(added_card)
    
    def shuffle_deck(self):
        random.shuffle(self.allCards)
    
    def deal_one_card(self, player=[], pile=[], deck=[]):
        try:
            return self.allCards.pop()
        except:
            print("No cards in deck, you must play a card")
            player_play(player,pile,deck)
    
    def reshuffle(self,card):
        self.allCards.append(card)

#Hand Class - Stores Card Classes
class Hand:
    
    def __init__(self):
        self.cards = []

        #Adds Card to "Hand"
    def add_card(self,card):
        self.cards.append(card)

    def place_card(self,loc):
        return self.cards.pop(loc)

class Pile:
    
    def __init__(self):
        self.cards = []

        #Adds Card to Pile
    def add_card(self,card):
        self.cards.append(card)

    def return_one_card(self):
        return self.cards.pop(0)
     
#Displays Player 1's view (# of Opp. Cards, card in play and cards in hand)
def player_one_view(player1,player2,pile,wild = "null"):
    print(f"Player 2 has {len(player2.cards)} cards\n")
    if pile.cards[-1].rank == "Eight":
        print("A wild card is in play!\n")
        print(f"The card in play is {str(pile.cards[-1])} but the suit is {wild}!")
    else:
        print(f"The card in play is {str(pile.cards[-1])}")
    print("\nYour Hand:")
    hand = []
    for card in player1.cards:
        hand.append(str(card))
    print(hand)

#Displays Player 2's view (# of Opp. Cards, card in play and cards in hand)
def player_two_view(player2,player1,pile,wild = "null"):
    print(f"Player 1 has {len(player1.cards)} cards\n")
    if pile.cards[-1].rank == "Eight":
        print(f"The card in play is {str(pile.cards[-1])} but the suit is {wild}!")
    else:
        print(f"The card in play is {str(pile.cards[-1])}")
    print("\nYour Hand:")
    hand = []
    for card in player2.cards:
        hand.append(str(card))
    print(hand)

#Checks to see if either player has won
def checkWin(player1,player2):
    if player1.cards == []:
        return False
    elif player2.cards == []:
        return False
    else:
        return True

#Function that allows the player to either choose to play or draw
def choice(player,pile,deck,wild="null"): 
    while True:
        user_input = input("\nWould you like to play a card or draw. Input 'draw' or 'play': \n")
        if user_input.lower() == "play":
            os.system('cls')
            player_play(player,pile,deck,wild)
            break
        elif user_input.lower() == "draw":
            os.system('cls')
            player_draw(player,pile,deck)
            break
        else:
            print("I don't understand your input, Try Again.\n")
            



#Function to allow the player to play a card
def player_play(player,pile,deck,wild="null"):
    playable_cards = []
    if pile.cards[-1].rank == "Eight":
        for i in player.cards:
            if i.suit == wild or i.rank == "Eight":
                playable_cards.append(str(i))
    else:
        for i in player.cards:
            if i.rank == pile.cards[-1].rank or i.suit == pile.cards[-1].suit or i.rank == "Eight":
                playable_cards.append(str(i))
    if playable_cards == []:
        print("No cards in your hand are playable, proceeding to draw a card.")
        null = input("\nPress Enter to Confirm.\n")
        os.system('cls')
        player_draw(player,pile,deck)
    else:
        print(playable_cards)
        while True:
            user_input = input("Type the name of the card you would like to play or type draw to draw instead. (Case-Sensative):\n")
            if user_input in playable_cards:
                for count, i in enumerate(player.cards):
                    if str(i) == user_input:
                        pile.add_card(player.place_card(count))
                break
            elif user_input.lower() == "draw":
                print("\n Drawing a card instead")
                null = input("\nPress Enter to Confirm.")
                os.system('cls')
                player_draw(player,pile,deck)
                break
            else:
               print("I don't understand your input, Try Again.\n")



#Function to allow a player to draw a card
def player_draw(player,pile,deck):
    player.add_card(deck.deal_one_card(player,pile,deck))
    if player.cards[-1].suit == pile.cards[-1].suit or player.cards[-1].rank == pile.cards[-1].rank:
        while True:
            user_input = input(f"\nThe card you picked up is the {str(player.cards[-1])} would you like to place it down? Yes or No?")
            if user_input.lower() == "no":
                break
            elif user_input.lower() == "yes":
                null = input(f"Placing down {player.cards[-1]}. Press Enter to Continue.:\n")
                pile.add_card(player.place_card(-1))
                break
            else:
               print("I don't understand your input, Try Again.\n")

    print("You Hand: ")
    hand = []
    for card in player.cards:
        hand.append(str(card))
    print(hand)

#Reshuffles deck from pile if out of cards in deck
def check_deck_count(deck,pile):
    if deck.allCards == []:
        for i in range(len(pile.cards) - 1):
            deck.reshuffle(pile.return_one_card())
        deck.shuffle_deck()
    else:
        pass

#Checks if the card that was played if an Eight and prompts a suit change
def check_wild(var):
    global init
    if discard_pile.cards[-1].rank == "Eight":
        if init:
            while True:
                change = input("\nWhat suit would you like to change the 8 to (Hearts, Spades, Diamonds or Clubs)?: \n")
                if change.lower() == "diamonds":
                    print("Changing to diamonds!\n")
                    return "Diamonds"
                elif change.lower() == "spades":
                    print("Changing to spades!\n")
                    return "Spades"
                elif change.lower() == "hearts":
                    print("Changing to hearts!\n")
                    return "Hearts"
                elif change.lower() == "clubs":
                    print("Changing to clubs!\n")
                    return "Clubs"
                else:
                    print("I don't understand your input, Try Again.\n")
                    
        else:
            return var
    else:
        init = True 


#Init (Sets up deck, discard pile and player hands)
while True:
    newDeck = Deck()
    newDeck.shuffle_deck()
    player_one_hand = Hand()
    player_two_hand = Hand()
    discard_pile = Pile()
    for i in range(5):
        player_one_hand.add_card(newDeck.deal_one_card())
        player_two_hand.add_card(newDeck.deal_one_card())
    discard_pile.add_card(newDeck.deal_one_card())
    if discard_pile.cards[-1].rank == "Eight":
        stop = input("I still work")
        newDeck.reshuffle(discard_pile.return_one_card())
        newDeck.shuffle_deck()
        discard_pile.add_card(newDeck.deal_one_card())
    break

#Game Logic - Player Turns
Playing = True
init = True
wild_suit = ""
start = True
while Playing:
    os.system('cls')
    if start:
        print("Welcome to Crazy Eights\n")
        start = False
    null = input("Player 1 press enter to when ready!")
    os.system('cls')
    player_one_view(player_one_hand,player_two_hand,discard_pile,wild_suit)
    choice(player_one_hand,discard_pile,newDeck,wild_suit)
    wild_suit = check_wild(discard_pile)
    null = input("\nPress Enter to end your turn")
    Playing = checkWin(player_one_hand,player_two_hand)
    check_deck_count(newDeck,discard_pile)
    if Playing:
        os.system('cls')
        null = input("Player 2's turn! Press Enter to continue")
        os.system('cls')
        player_two_view(player_two_hand,player_one_hand,discard_pile,wild_suit)
        choice(player_two_hand,discard_pile,newDeck,wild_suit)
        wild_suit = check_wild(discard_pile)
        null = input("\nPress Enter to end your turn")
        Playing = checkWin(player_one_hand,player_two_hand)
        check_deck_count(newDeck,discard_pile)

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
    if len(player_two_hand.cards) == 1:
        print(f"Player One had {len(player_one_hand.cards)} card left!")
    else:
        print(f"Player One had {len(player_one_hand.cards)} cards left!")