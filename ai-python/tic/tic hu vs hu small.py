# Tic Tac Toe hu vs hu


def main():
    intro()
    board = create_grid()
    printpretty(board)
    p1, p2 = sym()
    play(board, p1, p2)


def intro():
    print("Hello! Welcome to Tic Tac Toe game!")
    print()
    print("Rules: Player 1 and 2 are represented by X and O.")
    print("Matching any three in a row, column or diagonal wins.")
    print()
    input("Press Enter to continue...")
    print()


def create_grid():
    print("Here is the play Board:")
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def sym():
    p1 = input("Player 1, do you want to be X or O? ").upper()

    while p1 not in ["X", "O"]:
        p1 = input("Please enter X or O: ").upper()

    p2 = "O" if p1 == "X" else "X"
    print("Player 2 you are " + p2 + ".")

    input("Please press Enter to continue.")
    print()
    return p1, p2


def play(board, p1, p2):
    for count in range(1, 10):

        player = p1 if count % 2 == 1 else p2
        print("Player " + player + ", it's your turn")

        while True:
            row = int(input("Pick a row [0,1,2]: "))
            col = int(input("Pick a column [0,1,2]: "))

            if row not in range(3) or col not in range(3):
                print("Out of board, pick another position.")
            elif board[row][col] != " ":
                print("The square you picked is already filled, pick another.")
            else:
                break

        board[row][col] = player
        printpretty(board)

        if winner(board, player):
            print("Player " + player + " you won!!")
            print("Game over.")
            report(count, False, p1, p2)
            return

    print("The board is full, game over!")
    print("It's a tie.")
    report(9, True, p1, p2)


def winner(board, player):
    # Rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def printpretty(board):
    print("--+---+--")

    for row in board:
        print(row[0], "|", row[1], "|", row[2])
        print("--+---+--")


def report(count, tie, p1, p2):
    print()
    input("Press Enter to see the game summary...")

    if not tie:
        winner = p1 if count % 2 == 1 else p2
        print("Winner: Player " + winner)
    else:
        print("There is a tie.")


main()
