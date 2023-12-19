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
     
def player_one_view(player1,player2,pile,wild = "null"):
    """Displays Player 1's view (# of Opp. Cards, card in play and cards in hand)"""

    #Prints the card in play
    print(f"Player 2 has {len(player2.cards)} cards\n")
    if pile.cards[-1].rank == "Eight":
        print("A wild card is in play!\n")
        print(f"The card in play is {str(pile.cards[-1])} but the suit is {wild}!")
    else:
        print(f"The card in play is {str(pile.cards[-1])}")
    #Prints hand
    print("\nYour Hand:")
    hand = []
    for card in player1.cards:
        hand.append(str(card))
    print(hand)

def player_two_view(player2,player1,pile,wild = "null"):
    """Displays Player 2's view (# of Opp. Cards, card in play and cards in hand)"""

    #Prints the card in play
    print(f"Player 1 has {len(player1.cards)} cards\n")
    if pile.cards[-1].rank == "Eight":
        print(f"The card in play is {str(pile.cards[-1])} but the suit is {wild}!")
    else:
        print(f"The card in play is {str(pile.cards[-1])}")
    #Prints hand
    print("\nYour Hand:")
    hand = []
    for card in player2.cards:
        hand.append(str(card))
    print(hand)

def checkWin(player1,player2):
    """Checks to see if either player has won"""
    if player1.cards == []:
        return False
    elif player2.cards == []:
        return False
    else:
        return True

def choice(player,pile,deck,wild="null"): 
    """Function that allows the player to either choose to play or draw"""
    global played
    #Allows the play to decide to they want to draw a card or play a card
    while True:
        user_input = input("\nWould you like to play a card or draw. Input 'draw' or 'play': \n")
        if user_input.lower() == "play":
            os.system('cls')
            played = True #Sets played to True (For wild card organization)
            player_play(player,pile,deck,wild)
            break
        elif user_input.lower() == "draw":
            os.system('cls')
            player_draw(player,pile,deck)
            break
        else:
            print("I don't understand your input, Try Again.\n")
            

def player_play(player,pile,deck,wild="null"):
    """Function to allow the player to play a card"""

    global played

    #List of Playable Cards
    playable_cards = []
    #Checks to see the card in play is an Eight, if so, the onlys cards that can be played depend on the wild
    if pile.cards[-1].rank == "Eight":
        for i in player.cards:
            if i.suit == wild or i.rank == "Eight":
                playable_cards.append(str(i))

    #Adds cards that are playable to your hand
    else:
        for i in player.cards:
            if i.rank == pile.cards[-1].rank or i.suit == pile.cards[-1].suit or i.rank == "Eight":
                playable_cards.append(str(i))

    #If no playable cards are available, you will draw a card instead
    if playable_cards == []:
        print("No cards in your hand are playable, proceeding to draw a card.")
        played = False
        null = input("\nPress Enter to Confirm.\n")
        os.system('cls')
        player_draw(player,pile,deck)

    #If playable cards, the player is given a choice to play a card or draw
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
                played = False #Played it set to False
                print("\n Drawing a card instead")
                null = input("\nPress Enter to Confirm.")
                os.system('cls')
                player_draw(player,pile,deck)
                break
            else:
               print("I don't understand your input, Try Again.\n")


def player_draw(player,pile,deck,wild = "null"):
    """Function to allow a player to draw a card"""

    global played

    #Adds card to hand
    player.add_card(deck.deal_one_card(player,pile,deck))

    #If drawn card matches the suit or rank of the card in play, the player can place it down (For a wild card in play)
    if pile.cards[-1].rank == "Eight" and (player.cards[-1].suit == wild or player.cards[-1].rank == "Eight"):
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

    #If drawn card matches the suit or rank of the card in play, the player can place it down
    elif player.cards[-1].suit == pile.cards[-1].suit or player.cards[-1].rank == pile.cards[-1].rank:
        while True:
            user_input = input(f"\nThe card you picked up is the {str(player.cards[-1])} would you like to place it down? Yes or No?")
            if user_input.lower() == "no":
                break
            elif user_input.lower() == "yes":
                played = True;
                null = input(f"Placing down {player.cards[-1]}. Press Enter to Continue.:\n")
                pile.add_card(player.place_card(-1))
                break
            else:
               print("I don't understand your input, Try Again.\n")

    #Prints Finished Hand
    print("You Hand: ")
    hand = []
    for card in player.cards:
        hand.append(str(card))
    print(hand)

def check_deck_count(deck,pile):
    """Check if deck is empty and if so reshuffles the deck """
    if deck.allCards == []:
        for i in range(len(pile.cards) - 1):
            deck.reshuffle(pile.return_one_card())
        deck.shuffle_deck()
    else:
        pass

def check_wild(var):
    """Checks if the card that was played is an Eight and prompts a suit change"""
    global played
    if discard_pile.cards[-1].rank == "Eight":
        if played:
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
        played = False 


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
        stop = input("I still work")
        newDeck.reshuffle(discard_pile.return_one_card())
        newDeck.shuffle_deck()
        discard_pile.add_card(newDeck.deal_one_card())
    break

#Game Variables
Playing = True
played = False #Bool for if a card was played in the round
wild_suit = "" #Tracks the suit of the wild card
start = True #Bool to track the start of a new game

#Game Logic - Player Turns
while Playing:
    os.system('cls')
    if start:
        print("Welcome to Crazy Eights\n")
        start = False
    null = input("Player 1 press enter to when ready!")
    os.system('cls')
    #Prints Player View
    player_one_view(player_one_hand,player_two_hand,discard_pile,wild_suit)

    #Allows player to draw or play
    choice(player_one_hand,discard_pile,newDeck,wild_suit)

    #Checks if wild card was played in the round
    wild_suit = check_wild(discard_pile)
    null = input("\nPress Enter to end your turn")

    #Checks for win and reshuffle
    Playing = checkWin(player_one_hand,player_two_hand)
    check_deck_count(newDeck,discard_pile)

    #Game Logic - PLayer 2
    if Playing:
        os.system('cls')
        null = input("Player 2's turn! Press Enter to continue")
        os.system('cls')

        #Prints Player View
        player_two_view(player_two_hand,player_one_hand,discard_pile,wild_suit)

        #Allows player to draw or play
        choice(player_two_hand,discard_pile,newDeck,wild_suit)

        #Checks if wild card was played in the round
        wild_suit = check_wild(discard_pile)
        null = input("\nPress Enter to end your turn")

        #Checks for win and reshuffle
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