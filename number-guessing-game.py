import random

def number_guessing_game():
    number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print(f" Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"\n Game Over! The number was {number}.")

number_guessing_game()
