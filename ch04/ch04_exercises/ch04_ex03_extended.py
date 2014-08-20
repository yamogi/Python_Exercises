# Improve "Word Jumble" so that each word is paired with a
# hint. The player should be able to see the hint if he or
# she is stuck. Add a scoring system that rewards players
# who solve a jumble without asking for a hint.

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

SCORE = (0, 5, 10)

hint_activated = 0

# pick a random word and assign it to 'correct'
rand_index = random.randrange(len(WORDS))
word = WORDS[rand_index]
hint = HINTS[rand_index]
correct = word

# initialise empty string for jumble
jumble = ""

# create jumbled word (see ../word_jumble.py)
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
while guess != correct and guess != "":
    if guess == "?":
        print("Here is a hint:", hint)
        hint_activated = 1
    else:
        print("Sorry, that's not it.")

    guess = input("Guess (enter ? for hint): ")

if guess == correct:
    print("You got it!\n")
    if hint_activated == 1:
        print("You required a hint.")
        player_score = SCORE[1]
    else:
        print("Great! You didn't need a hint!")
        player_score = SCORE[2]
else:
    print("You didn't get the word...")
    print("\n\tWord was:", correct, "\n")
    player_score = SCORE[0]

print("Your score is:", str(player_score))

print("Thanks for playing")
