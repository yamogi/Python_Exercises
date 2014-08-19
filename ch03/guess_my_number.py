# Initial psuedocode:
#   pick a random number
#   while the player hasn't guessed the number
#     let the player guess
#   congratulate the player
#
# Stepwise refinement:
#   welcome the player to the game and explain it
#   pick a random number between 1 and 100
#   ask the player for a guess
#   set the number of guesses to 1
#     while the player's guess does not equal the number
#       if the guess is greater than the number
#         tell the player to guess lower
#       otherwise
#         tell the player to guess higher
#       get a new guess from the player
#       increase the number of guesses by 1
#   congratulate the player on guessing the number
#   let the player know how many guesses it took
#
#----------------------------------------------------------
# Guess my number
#
# The computer picks a random number between 1 and 100. The
# player tries to guess it and the computer lets the player
# know if the guess is too high, too low, or right on the
# money.
#----------------------------------------------------------

import random # importing the random module

print("\t Welcome to \"Guess My Number\"!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    print() # extra newline
    guess = int(input("Take a guess: "))
    tries += 1

print()
print("\tYou guessed it! The number was", the_number)
print("\tAnd it only took you", tries, "tries!")

input("\n\nPress enter to exit.")
