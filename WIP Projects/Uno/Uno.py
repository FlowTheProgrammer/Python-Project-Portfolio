import random
import os

colors = ('Red', 'Yellow', 'Green', 'Blue') 
ranks = ('1','2', '3', '4', '5', '6', '7', '8', '9', 'Ten', 'Skip','+2','Reverse')
wild_cards =  ('Wild','+4')
played = False #Bool for if a card was played in the round
skipped = False
reversed = False
needs_to_draw = False

#Card Class - Creates Cards
class Card():

    def __init__(self,color,rank):
        self.color = color
        self.rank = rank

    def __str__ (self):
        if self.color == 'Black':
            return f'{self.rank} Card'
        else:
            return f'{self.color} {self.rank}'


#Deck Class - Creates 52 Card Objects
class Deck():

    def __init__(self):

        self.allCards = []

        #Adds One 0 for each card
        for color in colors:
            added_card = Card(color,'0')
            self.allCards.append(added_card)

        #Adds all Number Cards
        for i in range(2):
            for color in colors:
                for rank in ranks:
                    added_card = Card(color,rank)
                    self.allCards.append(added_card)
        
        #Adds wild cards
        for card in wild_cards:
            for i in range(4):
                added_card = Card("Black",card)
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


def playerView(position,player_hand,players,pile,wild = "null"):
    """Displays Player's view (# of Opp. Cards, card in play and cards in hand)"""

    print("Cards in hand: ")
    for player in players:
        if player[0] != position:
            print(f"P{player[0]} - {len(player[1].cards)}")
    #Prints the card in play
    if pile.cards[-1].rank == "Wild" or pile.cards[-1].rank == "+4":
        print(f"\nThe card in play is a {str(pile.cards[-1])} but the color is {wild}!")
    else:
        print(f"\nThe card in play is a {str(pile.cards[-1])}")

    #Prints hand
    hand = []
    for card in player_hand.cards:
        hand.append(str(card))
    print(f"\nYour Hand: {sorted(hand)}")
    

def checkWin(players):
    """Checks to see if either player has won"""

    for player in players:
        if player[1].cards == []:
            return False
        else:
            return True


def choice(pos,player_hand,pile,deck,wild="null"): 
    """Function that allows the player to either choose to play or draw"""
    global played
    #Allows the play to decide to they want to draw a card or play a card
    while True:
        user_input = input("\nWould you like to play a card or draw. Input 'draw' or 'play': \n")
        if user_input.lower() == "play":
            os.system('cls')
            played = True #Sets played to True (For wild card organization)
            player_play(pos,player_hand,pile,deck,wild)
            break
        elif user_input.lower() == "draw":
            os.system('cls')
            player_draw(pos,player_hand,pile,deck,wild)
            break
        else:
            print("I don't understand your input, Try Again.\n")
            

def player_play(pos,player_hand,pile,deck,wild="null"):
    """Function to allow the player to play a card"""

    global played
    global skipped
    global reversed
    global needs_to_draw

    #List of Playable Cards
    playable_cards = []
    #Checks to see the card in play is an Eight, if so, the onlys cards that can be played depend on the wild
    if pile.cards[-1].rank == "Wild" or pile.cards[-1].rank == "+4":
        for i in player_hand.cards:
            if i.color == wild or i.rank == "Wild" or i.rank == "+4":
                playable_cards.append(str(i))

    #Adds cards that are playable to your hand
    else:
        for i in player_hand.cards:
            if i.rank == pile.cards[-1].rank or i.color == pile.cards[-1].color or i.rank == "Wild" or i.rank == "+4":
                playable_cards.append(str(i))

    #If no playable cards are available, you will draw a card instead
    if playable_cards == []:
        print("No cards in your hand are playable, proceeding to draw a card.")
        played = False
        null = input("\nPress Enter to Confirm.\n")
        os.system('cls')
        player_draw(pos,player_hand,pile,deck,wild)

    #If playable cards, the player is given a choice to play a card or draw
    else:
        print(playable_cards)
        while True:
            user_input = input("Type the name of the card you would like to play or type draw to draw instead. (Case-Sensative):\n")
            if user_input in playable_cards:
                for count, i in enumerate(player_hand.cards):
                    if str(i) == user_input:
                        if i.rank == 'Skip':
                            skipped = True
                        if i.rank == "Reverse":
                            reversed = True
                        if i.rank == '+4' or i.rank == "+2":
                            needs_to_draw = True
                        pile.add_card(player_hand.place_card(count))
                break
            elif user_input.lower() == "draw":
                played = False #Played it set to False
                print("\n Drawing a card instead")
                null = input("\nPress Enter to Confirm.")
                os.system('cls')
                player_draw(pos,player_hand,pile,deck,wild)
                break
            else:
               print("I don't understand your input, Try Again.\n")


def player_draw(pos,player_hand,pile,deck,wild = "null"):
    """Function to allow a player to draw a card"""

    global played

    #Adds card to hand
    player_hand.add_card(deck.deal_one_card(player_hand,pile,deck))

    #If drawn card matches the color or rank of the card in play, the player can place it down (For a wild card in play)
    if pile.cards[-1].rank == "Wild" or pile.cards[-1].rank == "+4": #Nested to skip over elif to avoid errors
        if (player_hand.cards[-1].color == wild or player_hand.cards[-1].rank == "Wild" or player_hand.cards[-1].rank == "+4"):
            pickupPlay(player_hand,pile)

    #If drawn card matches the color or rank of the card in play, the player can place it down
    elif player_hand.cards[-1].color == pile.cards[-1].color or player_hand.cards[-1].rank == pile.cards[-1].rank or player_hand.cards[-1].rank == "Wild" or player_hand.cards[-1].rank == "+4":
        pickupPlay(player_hand,pile)

    #Prints Finished Hand
    print("You Hand: ")
    hand = []
    for card in player_hand.cards:
        hand.append(str(card))
    print(hand)


def pickupPlay(player_hand,pile):
    global played
    """If drawn card matches the color or rank of the card in play, the player can place it down"""
    while True:
            user_input = input(f"\nThe card you picked up is the {str(player_hand.cards[-1])} would you like to place it down? Yes or No?")
            if user_input.lower() == "no":
                break
            elif user_input.lower() == "yes":
                played = True
                null = input(f"Placing down {player_hand.cards[-1]}. Press Enter to Continue.:\n")
                pile.add_card(player_hand.place_card(-1))
                break
            else:
               print("I don't understand your input, Try Again.\n")


def check_deck_count(deck,pile):
    """Check if deck is close to being empty and if so reshuffles the deck """
    if len(deck.allCards) <= 5:
        for i in range(len(pile.cards) - 1):
            deck.reshuffle(pile.return_one_card())
        deck.shuffle_deck()
    else:
        pass


def check_wild(var,pile):
    """Checks if the card that was played is an Eight and prompts a color change"""
    global played
    if pile.cards[-1].rank == "Wild" or pile.cards[-1].rank == "+4":
        if played:
            while True:
                played = False
                change = input("\nWhat color would you like to changeto (Blue, Green, Yellow, or Red)?: \n")
                if change.lower() == "blue":
                    print("Changing to blue!\n")
                    return "Blue"
                elif change.lower() == "green":
                    print("Changing to green!\n")
                    return "Green"
                elif change.lower() == "yellow":
                    print("Changing to yellow!\n")
                    return "Yellow"
                elif change.lower() == "red":
                    print("Changing to red!\n")
                    return "Red"
                else:
                    print("I don't understand your input, Try Again.\n")
                    
        else:
            return var
    else:
        played = False 


def skipPlayer():
    global skipped

    cpy = skipped
    skipped = False

    return cpy


def reversePlayer():
    global reversed

    cpy = reversed
    reversed = False

    return cpy


def drawCards():

    global needs_to_draw

    cpy = needs_to_draw
    needs_to_draw = False
    
    return cpy