import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"
winner = None
gameRunning = True

#printing the game board
def printboard(board):
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("-------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("-------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])

#take player's input
def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentplayer
    else:
        print("Oops! That spot is already used or invalid.")

#check for win or tie
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkCol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False
    
def checkTie(board):
    if "-" not in board:
        printboard(board)
        print("\nIt's a Tie!!")
        global gameRunning
        gameRunning = False

def checkWinner():
    if checkCol(board) or checkDiag(board) or checkRow(board):
        print(f"\nWinner is:  {winner}")
        global gameRunning
        gameRunning = False
        

#switch players
def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"
    
#computer move
def computer(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#check for win or tie again
while gameRunning:
    printboard(board)
    playerInput(board)
    checkWinner()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWinner()
    checkTie(board)
