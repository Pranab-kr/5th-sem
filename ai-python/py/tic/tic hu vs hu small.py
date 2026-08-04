#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Tic Tac Toe

def main():
    # This is main func
    intro()
    board = create_grid()
    printpretty(board)
    symbol_1, symbol_2 = sym()
    isfull(board, symbol_1, symbol_2)   # The func that starts the game


def intro():
    print("Hello! Welcome to Tic Tac Toe game!")
    print("\n")
    print("Rules: Player 1 and 2 are represented by X and O. Matching any three in a row, column or diagonal wins.")
    print("\n")
    input("Press Enter to continue...")
    print("\n")


def create_grid():
    # This func creates the blank playboard
    print("Here is the play Board:")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def sym():
    # This func decides the player's symbol
    symbol_1 = input("Player 1, do you want to be X or O? ").upper()

    while symbol_1 not in ["X", "O"]:
        symbol_1 = input("Please enter X or O: ").upper()

    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2 you are O.")
    else:
        symbol_2 = "X"
        print("Player 2 you are X.")

    input("Please press Enter to continue.")
    print()
    return (symbol_1, symbol_2)


def startGaming(board, symbol_1, symbol_2, count):
    # This func starts the game

    # Decide the turn
    if count % 2 == 1:
        player = symbol_1
    else:
        player = symbol_2

    print("Player " + player + ", it's your turn")

    row = int(input("Pick a row [0,1,2]: "))
    column = int(input("Pick a column [0,1,2]: "))

    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outofboard(row, column)
        row = int(input("Pick a row [0,1,2]: "))
        column = int(input("Pick a column [0,1,2]: "))

    # Check if the square is already filled
    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row [0,1,2]: "))
        column = int(input("Pick a column [0,1,2]: "))

        while (row > 2 or row < 0) or (column > 2 or column < 0):
            outofboard(row, column)
            row = int(input("Pick a row [0,1,2]: "))
            column = int(input("Pick a column [0,1,2]: "))

    # Locate player symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2

    return board


def isfull(board, symbol_1, symbol_2):
    count = 1
    winner = True

    while count <= 9 and winner:

        startGaming(board, symbol_1, symbol_2, count)
        printpretty(board)

        # Check if there is a winner
        winner = iswinner(board, symbol_1, symbol_2, count)

        if count == 9 and winner:
            print("The board is full, game over!")
            print("It's a tie.")

        count += 1

    if winner == False:
        print("Game over.")

    report(count - 1, winner, symbol_1, symbol_2)


def outofboard(row, column):
    print("Out of board, pick another position.")


def printpretty(board):
    rows = len(board)

    print("--+---+--")
    for r in range(rows):
        print(board[r][0], "|", board[r][1], "|", board[r][2])
        print("--+---+--")

    return board


def iswinner(board, symbol_1, symbol_2, count):
    winner = True

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol_1:
            winner = False
            print("Player " + symbol_1 + " you won!!")
            return winner

        elif board[row][0] == board[row][1] == board[row][2] == symbol_2:
            winner = False
            print("Player " + symbol_2 + " you won!!")
            return winner

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol_1:
            winner = False
            print("Player " + symbol_1 + " you won!!")
            return winner

        elif board[0][col] == board[1][col] == board[2][col] == symbol_2:
            winner = False
            print("Player " + symbol_2 + " you won!!")
            return winner

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == symbol_1) or \
       (board[0][2] == board[1][1] == board[2][0] == symbol_1):
        winner = False
        print("Player " + symbol_1 + " you won!!")
        return winner

    if (board[0][0] == board[1][1] == board[2][2] == symbol_2) or \
       (board[0][2] == board[1][1] == board[2][0] == symbol_2):
        winner = False
        print("Player " + symbol_2 + " you won!!")
        return winner

    return winner


def illegal(board, symbol_1, symbol_2, row, column):
    print("The square you picked is already filled, pick another.")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press Enter to see the game summary...")

    if winner == False:
        if count % 2 == 1:
            print("Winner: Player " + symbol_1)
        else:
            print("Winner: Player " + symbol_2)
    else:
        print("There is a tie.")


main()


# In[ ]:





# In[ ]:




