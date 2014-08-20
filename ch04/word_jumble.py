# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random # importing random module

# create a sequence of words to choose from
WORDS = ("python",
         "jumble",
         "easy",
         "difficult",
         "answer",
         "xylophone",
         "antidisestablishmentarianism")

# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# psuedocode for jumbling the word:
# ------------------------------------------------
# while the chosen word has letters in it
#     extract a random letter from the chosen word
#     add the random letter to the jumble word
# ------------------------------------------------

# create a jumbled version of the word
jumble = ""

while word: # until word is an empty string ("")...
    position = random.randrange(len(word)) # get a random index of word
    jumble += word[position] # concatenate this to the jumbled word
    # create a new version of word, minus the one letter at position 'position'
    # first slice = every letter up to but not including 'position'
    # second slice = every letter after 'position' to the end of the word
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
		Welcome to Word Jumble!

	Unscramble the letters to make a word.
	(Press the enter key at the prompt to quit).
"""
)

print("The jumble is:", jumble)

guess = input("\nYour guess: ")
# while the user hasn't guessed the word, and they haven't just pressed enter
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ") # let them guess again

# if they guessed it
if guess == correct:
    print("That's it! You guessed it!\n") # congratulate
else: # if they just pressed enter
    print("The word was:", correct, "\n") # comiserate

print("Thanks for playing.") # end
