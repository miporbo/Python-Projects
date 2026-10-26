# Number Guessing Game

A simple Python CLI game. The computer picks a secret number between
1 and 100, and you guess it. After every guess you get a hint (too low
or too high), and at the end you see how many attempts it took.

## Features
- Random secret number from 1 to 100
- Hints after every guess (too low / too high)
- Counts your attempts
- Invalid input (like text) does not crash the game and is not counted as an attempt
- Play again option at the end

## How to Run

python number_guessing_game.py

## Sample Output

I'm thinking of a number between 1 and 100.
Your guess: 50
Too low! Try again.
Your guess: abc
Please enter a whole number.
Your guess: 75
Too high! Try again.
Your guess: 62
Correct! You guessed it in 3 attempts.
Do you want to play again? (yes/no): no
Thanks for playing!

## Tech Used
- Python 3
- Core concepts: random module, while loop, break and continue, conditionals (if/elif/else), try/except, functions, f-strings

## Author
Md. Majharul Islam Porbo  
Portfolio: [porbo.cyou](https://porbo.cyou)
