# Create a game where the computer picks a random word and
# the player has to guess that word. the computer tells the
# player how many letters are in the word. Then the player
# gets five chances to ask if a letter is in the word. The
# computer can only respond with "yes" or "no". Then, the
# player must guess the word.

import random # importing the random module

WORDS = ("python",
         "jumble",
         "easy",
         "difficult",
         "answer",
         "xylophone")

word = random.choice(WORDS)

print(
"""
	Welcome to the Word Guess Game.
	Try to guess what word I am thinking of!
"""
)

print("There are", str(len(word)), "letters in the word...")

guess_count = 1

while guess_count <= 5:
    print("Guess a letter which might be in the word")
    letter_guess = input("(Attempt " + str(guess_count) + " of 5): ")

    if letter_guess.lower() in word.lower():
        print("   Yes")
    else:
        print("   No")

    guess_count += 1

print("\nYour guesses are up, time to try and guess the word")
word_guess = input()

print()

if word_guess.lower() == word.lower():
    print("You win!")
else:
    print("You lose!")
