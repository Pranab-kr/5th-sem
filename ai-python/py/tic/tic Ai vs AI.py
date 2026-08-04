#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import random
from time import sleep

# Create an empty board
def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

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
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board


# In[17]:


#check whether the player has three of the their marks in a horai row

def row_win(board,player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x,y] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)


# In[21]:


#check wheather the player has the three of their marks in vartical row

def col_win(board,player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if(board[y,x]) != player:
                win = False
                continue

        if win == True:
            return (win)
    return win



# In[9]:


# check wheather the player has three of their marks in diagonalrow

def diag_win(board,player):
    win = True
    y =0

    for x in range(len(board)):
        if board[x][x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) -1 -x
            if board[x,y] != player:
                win = False
    return win


# In[11]:


#Evaluate wheather there  is a winnner or tie

def evaluate(board):
    winner = 0

    for player in [1,2]:
        if (row_win(board,player) or col_win(board,player) or diag_win(board,player)):

            winner = player

        if np.all(board !=0 ) and winner == 0:
           winner = -1
        return winner


# In[26]:


# Main function to start the game
def play_game():
    board = create_board()
    winner = 0
    counter = 1

    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
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


# In[ ]:




