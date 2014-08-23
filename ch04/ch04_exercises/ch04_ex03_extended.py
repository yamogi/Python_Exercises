# ch04_ex03_extended.py
#
# Improve "Word Jumble" so that each word is paired with a hint. The player
# should be able to see the hint if he or she is stuck. Add a scoring system
# that rewards players who solve a jumble without asking for a hint.
#
# In this experimental version of the exercise, instead of providing the first
# letter of the word as a hint, I instead implemented a second HINTS tuple,
# where each index corresponds to the relevant word. In order to achieve this,
# I needed to pick a random index using randrange to ensure that WORDS and
# HINTS were working off of the same index value.
#

import random # importing random module

# initialise tuple of possible words
WORDS = ("python",
         "jumble",
         "easy",
         "difficult",
         "answer",
         "xylophone")

# initalise a tuple of corresponding hints
HINTS = ("it is a programming language",
         "it describes this game",
         "not difficult",
         "not easy",
         "what you're looking for",
         "a musical instrument")

SCORE = (0, 5, 10) # possible scores

hint_activated = 0 # has the hint been activated

# pick a random word and assign it to 'correct'
rand_index = random.randrange(len(WORDS)) # this is different to previous ver
word = WORDS[rand_index] # word and hint values obtained from same index
hint = HINTS[rand_index] # word and hint values obtained from same index
correct = word

# initialise empty string for jumble
jumble = ""

# create jumbled word (see ../word_jumble.py) comments
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print(
"""
	Welcome to the word jumble game.
"""
)

print("\nThe jumble is:", jumble)

guess = input("Guess (enter ? for hint): ")

# while word hasn't been guessed and user has not just pressed enter:
while guess != correct and guess != "":
    if guess == "?": # if user has asked for a hint
        print("Here is a hint:", hint) # provide the corresponding hint
        hint_activated = 1 # show that hint has been activated
    else: # otherwise, guess is incorrect
        print("Sorry, that's not it.")

    guess = input("Guess (enter ? for hint): ") # ask for another guess

if guess == correct: # if word has been guessed
    print("You got it!\n")
    if hint_activated == 1: # if user previously asked for a hint
        print("You required a hint.")
        player_score = SCORE[1] # assign score of 5
    else: # if no hint was required
        print("Great! You didn't need a hint!")
        player_score = SCORE[2] # assign score of 10
else: # if user pressed enter and quit the game
    print("You didn't get the word...")
    print("\n\tWord was:", correct, "\n") # assign score of 0
    player_score = SCORE[0]

print("Your score is:", str(player_score))

print("Thanks for playing")
