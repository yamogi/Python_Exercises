# Hangman Game
#
# The class game of Hangman. The computer picks a random word and the player
# tries to guess it, one letter at a time. If the player can't guess the word
# in time, the little stick figure gets hanged

import random # importing random module

# creating the ASCII art
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
----------
""")

# more constants
MAX_WRONG = len(HANGMAN) - 1 # number of times the player is allowed to fail
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON") # possible words

# initialise variables
word = random.choice(WORDS) # the word to be guessed
so_far = "-" * len(word)    # one dash for each letter in word to be guessed
wrong = 0                   # number of wrong guesses player has made
used = []                   # letters already guessed

# start the game
print("Welcome to Hangman. Good luck!")

# main loop
while wrong < MAX_WRONG and so_far != word:
# while the player still has guesses and the word hasn't been found...
    print(HANGMAN[wrong]) # print the current hangman ASCII art
    print("\nYou've used the following letters:\n", used) # print 'used' list
    print("\nSo far, the word is:\n", so_far) # print progress of word

    guess = input("\n\nEnter your guess: ") # enter a guess
    guess = guess.upper() # convert user's guess to uppercase

    while guess in used: # if the letter has been guessed before
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ") # make them guess again
        guess = guess.upper()

    used.append(guess) # once a new letter has been guessed, append to used

    if guess in word: # if guessed letter is in the word...
        print("\nYes!", guess, "is in the word!")
        # create a new so_far to include "guess"
        new = "" # initialise empty string
        for i in range(len(word)): # iterate through the hidden word
            if guess == word[i]: # if the guessed letter matches a letter
                new += guess # print out that letter and save to "new"
            else: # if guessed letter does NOT match a letter
                new += so_far[i] # put a dash instead (stolen from so_far[i])
        so_far = new # pass "new" onto "so_far"
    else: # if guessed letter is NOT in the word
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1 # increment the wrong counter

# 
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

# inform the user of the word, whether they guessed it or not
print("\nThe word was \"" + word + "\"")
