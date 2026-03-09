# Guess the Random Number 🎲

A console-based multiplayer guessing game built with Python.

## Description

Players take turns trying to guess a random number between 1 and 10. Points are won or lost depending on whether the guess is correct. At the end, a summary table shows each player's results.

## How It Works

- Each player starts with **50 points**
- Each turn, a random number (1–10) is generated
- **Correct guess** → earn `random number × 2` points
- **Wrong guess** → lose `random number` points
- At the end, results are displayed for all players

## How to Run

```bash
python guess_the_number.py
```

> No external dependencies required. Uses Python's built-in `random` library.

## Game Flow

```
1. Select number of players
2. Each player enters their name
3. Players take 3 turns each
4. Final scores are displayed
```

## Concepts Practiced

- Loops and conditionals
- Dictionaries and lists
- User input handling
- Basic exception handling

## Author

**Hernan Araya Lopez** — 2026-03-08
