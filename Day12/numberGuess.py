import random

from art import logo

# print logo
print(logo)

# Welcome intro
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

# A random number from 1 - 100
random_number = random.randint(1, 100)

# For Testing
print(f"Psst the number is {random_number}")

# Difficulty picker 10 if easy and 5 if hard
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    total_guess = 10
else:
    total_guess = 5

# Loops based on the difficulty
while total_guess >= 1:
    # Shows the Guess remaining
    print(f"You have {total_guess} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess != random_number:
        total_guess -= 1
        if guess > random_number:
            print("Too High.")
        elif guess < random_number:
            print("Too low.")
        elif guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            total_guess = 0
            exit()
        if total_guess == 0:
            print("You've run out of guesses, you lose.")
            exit()
    print("Guess again.")
