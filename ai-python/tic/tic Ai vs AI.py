import random
from time import sleep

import numpy as np


# Create an empty board
def create_board():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


# Check empty places on the board
def possibilities(board):
    I = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                I.append((i, j))

    return I


# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)

    # Choose a random empty position
    current_loc = random.choice(selection)

    board[current_loc] = player

    return board


# Check whether the player has three marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False

        if win:
            return True

    return False


# Check whether the player has three marks in a vertical column
def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y, x] != player:
                win = False

        if win:
            return True

    return False


# Check whether the player has three marks in a diagonal
def diag_win(board, player):

    # Main diagonal
    win = True

    for x in range(len(board)):
        if board[x, x] != player:
            win = False

    if win:
        return True

    # Other diagonal
    win = True

    for x in range(len(board)):
        y = len(board) - 1 - x

        if board[x, y] != player:
            win = False

    return win


# Evaluate whether there is a winner or tie
def evaluate(board):
    winner = 0

    # Check both players
    for player in [1, 2]:

        if row_win(board, player) or col_win(board, player) or diag_win(board, player):

            winner = player
            break

    # If board is full and nobody won
    if np.all(board != 0) and winner == 0:
        winner = -1

    return winner


# Main function to start the game
def play_game():

    board = create_board()
    winner = 0
    counter = 1

    print(board)
    sleep(2)

    while winner == 0:

        for player in [1, 2]:

            # Check if board is already full
            if len(possibilities(board)) == 0:
                winner = -1
                break

            board = random_place(board, player)

            print("Board after " + str(counter) + " move")
            print(board)

            sleep(2)

            counter += 1

            winner = evaluate(board)

            if winner != 0:
                break

    return winner


# Driver code
print("Winner is:", play_game())
