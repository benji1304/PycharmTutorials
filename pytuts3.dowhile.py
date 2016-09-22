# Guess a number between 1 and 10
# Keep asking until correct
# You guessed right!

# while loops and break statements

# Enter a number

import random

rand_num = random.randrange(1,11)
guess = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 10? "))
        if guess == rand_num:
            print("The random number was : ", rand_num)
            break

    except ValueError:
        print("You didn't even a number! Try again... ")

    except:
        print("An unknown error occurred")


