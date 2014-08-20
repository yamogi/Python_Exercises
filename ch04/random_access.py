# Random Access
# Demonstrates string indexing

import random # importing random module

word = "index" # setting word value
print("The word is, ", word, "\n")

high = len(word) # max index allowed
low = -len(word) # min index allowed

for i in range(10): # do this ten times
    position = random.randrange(low, high) # get a random string index
    print("word[", position, "]\t", word[position]) # print this
