import random

# func to print board


def print_board(board):

    for row in board:

        print("|".join(row))

        print("-" * 5)


# func to check for the winncheck_winner


# Function to check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True

    return False


# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


# Function to make the computer's move
def computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(available_moves)


# Function to handle a human's move
def human_move(board):
    while True:
        try:
            row, col = map(
                int, input("Enter row and column (0-2, space separated): ").split()
            )

            if board[row][col] == " ":
                return row, col
            else:
                print("Cell is already occupied, try again.")

        except (ValueError, IndexError):
            print(
                "Invalid input, please enter row and column as two numbers between 0 and 2."
            )


# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print_board(board)

    while True:
        # Human's turn
        row, col = human_move(board)
        board[row][col] = "X"

        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations, you win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn...")

        row, col = computer_move(board)
        board[row][col] = "O"

        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break


# Run the game
if __name__ == "__main__":
    play_game()
