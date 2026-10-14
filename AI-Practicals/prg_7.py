# Two-Player Tic-Tac-Toe Using a Heuristic Function

# Initialize the game board
board = [" " for _ in range(9)]

# Winning combinations: rows, columns, and diagonals
winning_lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


# Display the game board
def display_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


# Check whether a player has won
def check_winner(player):
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


# Heuristic function to evaluate the board
def heuristic(player):
    opponent = "O" if player == "X" else "X"
    score = 0

    for a, b, c in winning_lines:
        line = [board[a], board[b], board[c]]

        # Reward lines that can still be completed by the player
        if opponent not in line:
            score += line.count(player) ** 2

        # Penalize lines that can be completed by the opponent
        if player not in line:
            score -= line.count(opponent) ** 2

    return score


# Play the game
current_player = "X"

while True:
    display_board()
    print("Player", current_player)
    print("Heuristic score:", heuristic(current_player))

    try:
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position. Try again.\n")
            continue

    except ValueError:
        print("Enter a valid number.\n")
        continue

    board[position] = current_player

    # Check for a win
    if check_winner(current_player):
        display_board()
        print("Player", current_player, "wins!")
        break

    # Check for a draw
    if " " not in board:
        display_board()
        print("Game is a draw!")
        break

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"
