import random

# Generate the secret number
secret_number = random.randint(1, 99)

print("I am now thinking of a number between 1 and 99")

# User's guess
guess = int(input("Enter your guess: "))

# Keep asking until correct
while guess != secret_number:

    if guess < secret_number:
        print("Your guess is too low")

    else:
        print("Your guess is too high!")

    guess = int(input("Enter a new guess: "))

print("Congrats! The number was:", secret_number)
