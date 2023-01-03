import os

#Welcome Message :)
print("Welcome to Tic Tac Toe")

# Creates the TicTacToe Board
game_board = ["PlaceHolder"," "," "," "," "," "," "," "," "," "]
validSpace = ["1","2","3","4","5","6","7","8","9"]
game_on = True

#Askes User for X or O (Player 1 goes first)
player1 = input("Player 1: Would you like to be X or O?").upper()
validInputs = ["X","O"]
os.system('cls')

while player1 not in validInputs:
    print("Sorry, that is not a valid input")
    player1 = input("Would you like to be X or O")
    os.system('cls')

#Creates player2 (Make P2 "X" if P1 is "O" and vice versa)
player2 = "X" if player1 == "O" else "O"

#Displays the board
def  display_game(board):
    print(board[7] + "|" + board[8] + "|"  + board[9])
    print("-----")
    print(board[4] + "|" + board[5] + "|"  + board[6])
    print("-----")
    print(board[1] + "|" + board[2] + "|"  + board[3])

#Checks the validity of user inputs
def position_choice():
    choice = ""
    while choice not in validSpace:
        choice = input("Pick a position 1-9")
        if choice not in validSpace:
            os.system('cls')
            print("Sorry, invalid choice!")
            display_game(game_board)


    validSpace.remove(choice)
    return int(choice)

#Replaces the list index with "X" or "O" based on user input
def replacement_choice(game_board,position,player):
    
    user_placement = player
    
    game_board[position] = user_placement
    
    return game_board


#Checks if P1 or P2 has won
def checkWin(board, p1 , p2):
    wins = [[board[1],board[2],board[3]],[board[4],board[5],board[6]],[board[7],board[8],board[9]],[board[1],board[4],board[7]],
    [board[2],board[5],board[8]],[board[3],board[6],board[9]],[board[3],board[5],board[7]],[board[1],board[5],board[9]]]
    player1Win = [p1,p1,p1]
    player2Win = [p2,p2,p2]
    playerDraw = 0

    #Loops to find a Win or Draw
    for i in wins:
        if player1Win == (i):
            print ("Player 1 Wins!")
            return False
        elif player2Win == (i):
            print ("Player 2 Wins!")
            return False
    for i in wins:
        if " " not in i:
            playerDraw += 1
        if playerDraw == 8:
            print("It's a Draw!")
            return False
    return True

#Initializes Game
while game_on:
    display_game(game_board)
    pos = position_choice()
    os.system('cls')
    game_board = replacement_choice(game_board, pos, player1)
    display_game(game_board)
    game_on = checkWin(game_board,player1,player2)
    if game_on:
        pos = position_choice()
        os.system('cls')
        game_board = replacement_choice(game_board, pos, player2)
        game_on = checkWin(game_board,player1,player2)

#Add replayability