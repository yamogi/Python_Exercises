# Modify the Guess My Number game so that the player has a
# limited number of guesses. If the player fails to guess
# in time, the program should display an appropriately
# chastising message.

import random # importing the random module

print("\t Welcome to \"Guess My Number\"!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1
guess_limit = 10

# guessing loop
while guess != the_number and tries < guess_limit:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    print() # extra newline
    guess = int(input("Take a guess: "))
    tries += 1

if guess == the_number:
    print()
    print("\tYou guessed it! The number was", the_number)
    print("\tAnd it only took you", tries, "tries!")
else:
    print("\n\tYou failed to guess within the number of guesses (" + str(guess_limit) + ") allowed!")

input("\n\nPress enter to exit.")
