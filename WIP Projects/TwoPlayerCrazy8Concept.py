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
     
#Displays Player 1's view (# of Opp. Cards, card in play and cards in hand) (Functional)
def player_one_view(player1,player2,pile):
    print(f"Player 2 has {len(player2.cards)} cards\n")
    print(f"The card in play is {str(pile.cards[-1])}")
    print("\nYour Hand:")
    hand = []
    for card in player1.cards:
        hand.append(str(card))
    print(hand)

#Displays Player 2's view (# of Opp. Cards, card in play and cards in hand) (Functional)
def player_two_view(player2,player1,pile):
    print(f"Player 1 has {len(player1.cards)} cards\n")
    print(f"The card in play is {str(pile.cards[-1])}")
    print("\nYour Hand:")
    hand = []
    for card in player2.cards:
        hand.append(str(card))
    print(hand)

#Checks to see if either player has won (Haven't checked)
def checkWin(player1,player2):
    if player1.cards == []:
        return False
    elif player2.cards == []:
        return False
    else:
        return True

#Function that allows the player to either choose to play or draw (Functional)
def choice(player,pile,deck): 
    while True:
        user_input = input("Would you like to play a card or draw. Input 'draw' or 'play'")
        if user_input.lower() == "play":
            os.system('cls')
            player_play(player,pile,deck)
            break
        elif user_input.lower() == "draw":
            os.system('cls')
            player_draw(player,pile,deck)
            break
        else:
            print("I don't understand your input, Try Again.\n")
            



#Function to allow the player to play a card (Functional)
def player_play(player,pile,deck):
    playable_cards = []
    for i in player.cards:
        if i.rank == pile.cards[-1].rank or i.suit == pile.cards[-1].suit:
            playable_cards.append(str(i))
    if playable_cards == []:
        print("No cards in your hand are playable, proceeding to draw a card.")
        null = input("\nPress Enter to Confirm.")
        os.system('cls')
        player_draw(player,pile,deck)
    else:
        print(playable_cards)
        while True:
            user_input = input("Type the name of the card you would like to play or type draw to draw instead. (Case-Sensative)")
            if user_input in playable_cards:
                for count, i in enumerate(player.cards):
                    if str(i) == user_input:
                        pile.add_card(player.place_card(count))
                break
            elif user_input.lower == "draw":
                print("\n Drawing a card instead")
                null = input("\nPress Enter to Confirm.")
                os.system('cls')
                player_draw(player,pile,deck)
                break
            else:
               print("I don't understand your input, Try Again.\n")
    null = input("Press Enter to end your turn")



#Function to allow a player to draw a card (Functional)
def player_draw(player,pile,deck):
    player.add_card(deck.deal_one_card())
    print("You new hand is: ")
    hand = []
    for card in player.cards:
        hand.append(str(card))
    print(hand)
    null = input("\n Press Enter when you want to end your turn.")

#Reshuffles deck from pile if out of cards (Haven't checked)
def check_deck_count(deck,pile):
    if deck.allCards == 0:
        for i in len(pile.cards) - 1:
            deck.reshuffle(pile.return_one_card)
    else:
        pass


#Init
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
    check_deck_count(newDeck,discard_pile)
    if Playing:
        os.system('cls')
        null = input("Player 2's turn! Press Enter to continue")
        os.system('cls')
        player_two_view(player_two_hand,player_one_hand,discard_pile)
        choice(player_two_hand,discard_pile,newDeck)
        Playing = checkWin(player_one_hand,player_two_hand)
        check_deck_count(newDeck,discard_pile)
    break #Remove when done