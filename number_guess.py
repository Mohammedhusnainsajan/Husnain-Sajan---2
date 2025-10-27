import random

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

guess = None

while guess != number_to_guess:
    guess = int(input("Enter your guess (1-100): "))

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
