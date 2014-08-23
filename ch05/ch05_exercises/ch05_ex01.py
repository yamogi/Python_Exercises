# ch05_ex01.py
#
# Create a program that prints a list of words in random order. The program
# should print all the words and not repeat any.
#

import random # importing random module

WORDS = ("one", # initialise WORDS tuple (immutable)
         "two",
         "three",
         "four",
         "five",
         "six",
         "seven",
         "eight")

max_word_count = len(WORDS) # max number of words, for the while loop
word_counter = 0 # initialising a loop counter
USED_WORDS = [] # empty list for when a word has been used

while word_counter < max_word_count: # while there are still words to be said
    random_word = random.choice(WORDS) # pick a random word

    if random_word in USED_WORDS: # if word has already been said
        random_word = random.choice(WORDS) # pick a random word
    else: # if word has not yet been said
        print("\t", random_word) # print the word
        USED_WORDS.append(random_word) # keep track of used words
        word_counter += 1 # increment the loop counter
