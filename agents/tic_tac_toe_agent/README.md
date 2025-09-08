# Tic‑Tac‑Toe Agent

An example of an **autonomous game‑playing agent**.  This skeleton plays
tic‑tac‑toe against a human user or another agent.  Use it to explore
planning, decision‑making and reinforcement learning with a simple game.

## Features

- Defines the tic‑tac‑toe board and valid moves.
- Implements a basic game loop where the agent selects a move based on
  predefined rules or heuristics.
- Provides hooks for integrating more advanced decision methods (e.g.,
  minimax, Monte Carlo tree search, reinforcement learning).

## Setup

No extra dependencies are required for the basic implementation.  You can
install `numpy` if you wish to use arrays for the board representation:

```bash
pip install numpy
```

## Usage

Run the agent with:

```bash
python main.py
```

You will be prompted to choose whether the agent goes first or second.  The
game will then proceed until either player wins or the board is full.  The
current implementation plays randomly; feel free to implement smarter logic
in `main.py`.

## Extending the agent

- Implement the minimax algorithm or Q‑learning to make the agent play
  optimally.
- Modify the game loop to support remote play or self‑play for training.
- Use this skeleton as a template for other games (e.g., connect four,
  chess puzzles).
