# ch04_ex04.py
#
# Create a game where the computer picks a random word and
# the player has to guess that word. the computer tells the
# player how many letters are in the word. Then the player
# gets five chances to ask if a letter is in the word. The
# computer can only respond with "yes" or "no". Then, the
# player must guess the word.
#

import random # importing the random module

WORDS = ("python", # tuple of possible words
         "jumble",
         "easy",
         "difficult",
         "answer",
         "xylophone")
MAX_GUESS_COUNT = 5 # max guesses allowed
guess_count = 0 # initial guess counter

word = random.choice(WORDS) # pick a random word

print(
"""
	Welcome to the Word Guess Game.
	Try to guess what word I am thinking of!
"""
)

# count number of letters in the chosen word
print("There are", str(len(word)), "letters in the word...")

while guess_count < MAX_GUESS_COUNT:
    guess_count += 1 # increment guess counter

    print("Guess a letter which might be in the word")
    letter_guess = input("(Attempt " + str(guess_count) + " of 5): ")

    if letter_guess.lower() in word.lower(): # convert both to lowercase
        print("   Yes")
    else:
        print("   No")

print("\nYour guesses are up, time to try and guess the word")
word_guess = input()

print()

if word_guess.lower() == word.lower(): # convert both to lowercase
    print("You win!")
else:
    print("You lose!")
