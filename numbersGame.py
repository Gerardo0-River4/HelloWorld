"""
Documentation
"""

import random

secret = random.randint(1,99)

guess = 0
count = 0

print("Guess a number between 1 and 99.")


while guess != secret and count < 6:
    guess = int(input())
    if guess < secret:
        print("Too low, guess higher!")
    elif guess > secret:
        print("Too high, guess lower!")
    count = count + 1
    print("tries: " , count)


if guess == secret:
    print("YOU WON! GOOD JOBERT ROBERT!")

else :
    print("Sorry, no more guesses, you lose.\n")
    print("The number was " ,secret,"!")