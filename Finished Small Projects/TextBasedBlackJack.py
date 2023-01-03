import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
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
        self.aces = 0

        #Adds Card to "Hand"
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        #Used to track ace #
        if card.rank == "Ace":
            self.aces += 1
    #Used to change value of Ace from 11 to 1
    def special_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    def __init__(self):
        self.chips = 100
        self.bet = 0

    def loss(self):
        self.chips = self.chips - self.bet
    
    def win(self):
        self.chips = self.chips + self.bet


def player_bet(chips):
    while True:
        try: 
            num = int(input("How much would you like to bet?"))
            while num < 0 or num > chips.chips:
                while True:
                    try:
                        print(f"\nPlease enter a number that is greater than 0 and less than {chips.chips}\n")
                        num = int(input("How much would you like to bet?"))
                        break
                    except:
                        print("Invalid Input\n")        
            break
        except:
            print("Invalid Input\n")

def hit_or_pass(deck,hand):
    global gambling
    global didHit

    while True:
        choice = input("\nWould you like to hit or pass?")

        if choice.lower() == "hit":
            hit(deck,hand)
        elif choice.lower() == "pass":
            print("You ended your turn. The Dealer now plays")
            gambling = False
            didHit = False
        else:
            print("Unknown Input, Try Again.")
            continue
        break

def hit(deck,hand):
    card = deck.deal_one_card()
    hand.add_card(card)
    hand.special_ace()


def check_if_bust(hand):
    if hand.value > 21:
        print("You have busted, the dealer wins")
        return False

def player_turn_cards(dealer,player):
    print("\nDealer's Hand: ")
    print("First Card is Face Down")
    print(dealer.cards[1])

    print("\n Your Hand:")
    for card in player.cards:
        print(card)

def dealer_turn_cards(dealer,player):
    print("\n Your Hand:")
    for card in player.cards:
        print(card)

    print("\n Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print(f"The value of the Dealer's hand is {dealer.value}")

#Winning Options

def player_bust(player,dealer,chips):
    print("You have busted")
    chips.loss()

def player_wins(player,dealer,chips):
    print("You have won!")
    chips.win()

def dealer_busts(player,dealer,chips):
    print("The Dealer has busted!")
    chips.win()

def dealer_wins(player,dealer,chips):
    print("The Dealer has won")
    chips.loss()
def tie(player,dealer,chips):
    print("It was a tie!")

gambling = True
Ready = True
didHit = True

while Ready:
    print("Welcome to BlackJack\n\n")
    newDeck = Deck()
    newDeck.shuffle_deck()
    dealerHand = Hand()
    playerHand = Hand()
    for i in range(2):
        dealerHand.add_card(newDeck.deal_one_card())
        playerHand.add_card(newDeck.deal_one_card())
    playerChips = Chips()
    player_bet(playerChips)
    player_turn_cards(dealerHand,playerHand)
    Ready = False

while gambling:
    #Some Function To Start Game
    hit_or_pass(newDeck,playerHand)
    if didHit:
        player_turn_cards(dealerHand,playerHand)

    if playerHand.value > 21:
        player_bust(playerHand,dealerHand,playerChips)
        break

if playerHand.value < 21:

    while dealerHand.value < 17:
        hit(newDeck,dealerHand)
        
    dealer_turn_cards(dealerHand,playerHand)

    if playerHand.value > dealerHand.value:
        player_wins(playerHand,dealerHand,playerChips)
    elif dealerHand.value > 21:
            dealer_busts(playerHand,dealerHand,playerChips)
    elif playerHand.value < dealerHand.value:
        dealer_wins(playerHand,dealerHand,playerChips)
    elif playerHand.value == dealerHand.value:
        tie(playerHand,dealerHand,playerChips)
