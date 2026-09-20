# Number Guessing Game

A simple command-line number guessing game built with Python.

## Features

- Generates a random number between 1 and 100
- Allows the player to make repeated guesses
- Provides hints when a guess is too high or too low
- Ends when the correct number is guessed

## Requirements

- Python 3.x
- No external dependencies

## How to Run

Navigate to the project directory and run:

```bash
python main.py
```

## How to Play

1. Run the program.
2. Guess a number between 1 and 100.
3. The game tells you whether your guess is too high or too low.
4. Keep guessing until you find the correct number.

## Example

```text
Welcome to the Number Guessing Game!

Guess a number between 1 and 100: 50
Too high! Try again.

Guess a number between 1 and 100: 25
Too low! Try again.

Guess a number between 1 and 100: 37
Congratulations! You guessed the number.
```

## Current Limitations

- The number range is fixed to 1–100.
- Invalid input is not currently handled.
- The number of attempts is not tracked.
- There is currently no difficulty system or scoring system.
- The current program does not actually handle `exit` as the prompt suggests.

## Future Improvements

Potential improvements may include:

- Track the number of attempts
- Add a scoring system
- Add difficulty levels
- Allow the player to choose the number range
- Add input validation
- Add a play-again option

## Project Status

This is a learning project created while learning Python. The project may be expanded and improved over time.

## Technologies

- Python
- `random` module