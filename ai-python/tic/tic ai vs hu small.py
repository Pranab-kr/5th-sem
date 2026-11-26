import random


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][2 - i] == player for i in range(3)) or all(
        board[i][i] == player for i in range(3)
    ):
        return True
    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def computer_move(board):
    available_move = [
        (i, j) for i in range(3) for j in range(3) if board[i][j] == " "
    ]
    return random.choice(available_move)


def human_move(board):
    while True:
        try:
            row, col = map(
                int, input("Enter row col (0-2), space separated :").split()
            )
            if board[row][col] == " ":
                return row, col
            else:
                print("cell is already occupied try again!")
        except (ValueError, IndexError):
            print("Invalid input")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        row, col = human_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulation you win!")
            break
        if is_board_full(board):
            print("It is a tie!")
            break
        print("Computer's turn...")
        row, col = computer_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It is a tie!")
            break


if __name__ == "__main__":
    play_game()