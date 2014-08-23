# ch04_ex04.py
#
# Here's a bigger challenge. Write the psuedocode for a program where the
# player and the computer trade places in the number guessing game. That is,
# the player picks a random number between 1 and 100 that the computer has to
# guess. Before you start, think about how you guess. If all goes well, try
# coding the game.
#
#----------------------------------------------------------
# Psuedocode
#----------------------------------------------------------
# player thinks of a number between 1 and 100
# computer guesses a number between 1 and 100
#   new random.randint is (min, max)
# player evaluates the computer's guess
#   if the guess is HIGHER than the player's number
#     reassign their guess as the new minimum (+1)
#   if the guess is LOWER than the player's number
#     reassign their guess as the new maximum (-1)
# congratulate the computer
#----------------------------------------------------------

import random # importing the random module

print("Hello! I am the computer!")
print("Please think of a number between 1 and 100")

# initialising values
min = 1 # initial min value
max = 100 # initial max value
tries = 0 # initial tries counter
hint = 0 # initial hint value

while hint != 3: # while the number hasn't been guessed
    tries += 1 # increment tries value

    # generate a random integer using current min/max values
    guess = random.randint(min,max)

    print()
    print("I am thinking of the number...")
    print("\t" + str(guess))
    print("Should I guess higher or lower?")
    # player specifies if the number is too low, too high, or a match
    hint = int(input("1 for higher, 2 for lower, 3 for match: "))

    # (note the inclusion of (+1) and (-1))
    # (this is to ensure that the same number is not guessed again)
    if hint == 1: # if number needs to be HIGHER
        min = guess + 1 # reassign their guess as the new MINIMUM (+1)
    elif hint == 2: # if number needs to be LOWER
        max = guess - 1 # reassign their guess as the new MAXIMUM (-1)
    elif hint == 3: # if guess is correct
        break # break out of the loop (could also have used continue)
    else: # default fail condition
        print("Illegal hint value")

print()
print("\tHooray! I guessed the number!")
print("\tAnd it only took me " + str(tries) + " tries!\n")
