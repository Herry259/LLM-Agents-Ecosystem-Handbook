"""Tic‑Tac‑Toe Agent

This script implements a simple tic‑tac‑toe game where the agent plays
against a human.  The agent’s strategy is currently random; replace the
`choose_move` function with smarter logic (e.g., minimax) to improve
performance.
"""

import random


def print_board(board):
    """Display the current board state."""
    symbols = {None: " ", "X": "X", "O": "O"}
    for row in board:
        print("|".join(symbols[cell] for cell in row))
        print("-" * 5)


def check_winner(board):
    """Return 'X', 'O' or None if there is a winner, otherwise return None."""
    lines = []
    # rows and columns
    lines.extend(board)
    lines.extend(list(zip(*board)))
    # diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] and all(cell == line[0] for cell in line):
            return line[0]
    return None


def choose_move(board, mark):
    """Choose a random valid move for the agent."""
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
    return random.choice(empty_positions)


def main():
    print("Welcome to Tic‑Tac‑Toe!\n")
    agent_mark = random.choice(["X", "O"])
    user_mark = "O" if agent_mark == "X" else "X"
    print(f"The agent will be '{agent_mark}'. You are '{user_mark}'.")
    # Set up empty board
    board = [[None, None, None] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == agent_mark:
            i, j = choose_move(board, agent_mark)
            print(f"Agent chooses position ({i}, {j}).")
        else:
            # Human move
            move = input("Enter your move as row,col (0‑2): ")
            try:
                i, j = map(int, move.split(","))
            except ValueError:
                print("Invalid input. Please enter row,col like 0,2.")
                continue
            if i not in range(3) or j not in range(3) or board[i][j] is not None:
                print("Invalid move. Try again.")
                continue
        board[i][j] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == agent_mark:
                print("Agent wins!")
            else:
                print("You win!")
            break
        if all(board[i][j] is not None for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
