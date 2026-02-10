# Python Project Idea – Make a program which randomly chooses a number to guess
# and then the user will have a few chances to guess the number correctly.
# In each wrong attempt, the computer will give a hint that the number is
# greater or smaller than the one you have guessed.
# use random.randint

import random

# Computer randomly chooses a number
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Try a smaller number than guess number.\n")
    else:
        print("Try a greater number than guess number.\n")
