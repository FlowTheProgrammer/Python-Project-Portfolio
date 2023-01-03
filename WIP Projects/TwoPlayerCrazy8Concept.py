import random
import os

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':1}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 

#Card Class - Creates Cards
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

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
    
    def deal_one_card(self):
        return self.allCards.pop()

#Hand Class - Stores Card Classes
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0

        #Adds Card to "Hand"
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

class Pile:
    
    def __init__(self):
        self.cards = []

        #Adds Card to Pile
    def add_card(self,card):
        self.cards.append(card)
     
def player_one_view(player1,player2,pile):
    print(f"Player 2 has {len(player2.cards)} cards\n")
    print(f"The card in play is {str(pile.cards[-1])}")
    print("\nYour Hand:")
    hand = []
    for card in player1.cards:
        hand.append(str(card))
    print(hand)

def player_two_view(player2,player1,pile):
    print(f"Player 1 has {len(player1.cards)} cards\n")
    print(f"The card in play is {str(pile.cards[-1])}")
    print("\nYour Hand:")
    hand = []
    for card in player2.cards:
        hand.append(str(card))
    print(hand)

def checkWin(player1,player2):
    if player1.cards == []:
        return False
    elif player2.cards == []:
        return False
    else:
        return True

#Might edit to have drawing and playing be two different functions
def choice(player,pile,deck):
    while True:
        user_input = input("Would you like to play a card or draw. Input 'draw' or 'play'")
        if user_input.lower() == "play":
            os.system('cls')
            play_or_draw(user_input.lower())
            break
        elif user_input.lower() == "draw":
            os.system('cls')
            play_or_draw(user_input.lower())
            break
        else:
            print("I don't understand your input, Try Again.\n")
            #Maybe edit this so that it clears everything and reprints game

def play_or_draw(x):
    pass

def check_deck_count():
    pass


while True:
    print("Welcome to Crazy Eights")
    newDeck = Deck()
    newDeck.shuffle_deck()
    player_one_hand = Hand()
    player_two_hand = Hand()
    discard_pile = Pile()
    for i in range(5):
        player_one_hand.add_card(newDeck.deal_one_card())
        player_two_hand.add_card(newDeck.deal_one_card())
    discard_pile.add_card(newDeck.deal_one_card())
    break

Playing = True
while Playing:
    os.system('cls')
    null = input("Player 1 press enter to when ready!")
    os.system('cls')
    player_one_view(player_one_hand,player_two_hand,discard_pile)
    choice(player_one_hand,discard_pile,newDeck)
    Playing = checkWin(player_one_hand,player_two_hand)
    #checkDeckCount
    if Playing:
        os.system('cls')
        null = input("Player 2's turn! Press Enter to continue")
        os.system('cls')
        player_two_view(player_two_hand,player_one_hand,discard_pile)
        choice(player_two_hand,discard_pile,newDeck)
        Playing = checkWin(player_one_hand,player_two_hand)
        check_deck_count()
    break