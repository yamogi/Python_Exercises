# ch03_ex03.py
#
# Modify the Guess My Number game so that the player has a limited number of
# guesses. If the player fails to guess in time, the program should display an
# appropriately chastising message.
#

import random # importing the random module

print("\t Welcome to \"Guess My Number\"!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1,100) # picking a random number
guess = int(input("Take a guess: ")) # obtaining user's guess
tries = 0 # number of attempts
guess_limit = 10 # max number of guesses

# guessing loop
# while number has not been guessed and user still has guesses:
while guess != the_number and tries < guess_limit:
    tries += 1 # increment attempts counter

    if guess > the_number: # if guess is higher
        print("Lower...") # make the user guess lower
    else: # if guess is lower
        print("Higher...") # make the user guess higher

    print() # extra newline
    print("You have", str(guess_limit - tries), "guesses left!")
    guess = int(input("Take a guess: ")) # obtain another guess

if guess == the_number: # if number is guessed
    tries += 1 # increment attempts counter
    print() # extra newline
    print("\tYou guessed it! The number was", the_number)
    print("\tAnd it only took you", tries, "tries!")
else: # if number has NOT been guessed
    print("\n\tYou failed to guess within the number of guesses (" + str(guess_limit) + ") allowed!")

input("\n\nPress enter to exit.")
