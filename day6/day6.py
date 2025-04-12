# Day 6: Number Guessing Game

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)  # Random number between 1 and 20
    guess = 0  # Initialize guess variable

    while guess != secret_number:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")

    print("Congratulations! You guessed the number correctly. 🎉")

# Run the game
number_guessing_game()