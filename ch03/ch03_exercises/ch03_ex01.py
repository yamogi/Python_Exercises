# ch03_ex01.py
#
# Write a program that simulates a fortune cookie. The program should display
# one of five unique fortunes, at random, each time it's run.
#

import random # importing the random module

fortune = random.randint(1,5) # pick a random number between 1 and 5

print("\n\t", end="")

if fortune == 1:
    print("You will have good luck today!")
elif fortune == 2:
    print("You will forget something today!")
elif fortune == 3:
    print("You will find love today!")
elif fortune == 4:
    print("You will be successful today!")
elif fortune == 5:
    print("You will encounter sadness today!")
else: # if outside the range of 1 to 5 (impossible)
    print("You have no fortune today!")

input("\nPress enter to exit.")
