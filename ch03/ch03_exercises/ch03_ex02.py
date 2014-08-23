# ch03_ex02.py
#
# Write a program that flips a coin 100 times and then tells you the number of
# heads and tails.
#

import random # import the random module

# initialising values
flip_count = 0
coin = 0
heads = 0
tails = 0

while flip_count < 100: # while flipping 100 times
    coin = random.randint(1, 2) # coin is either 1 or 2

    if coin == 1: # if 1
        heads += 1 # increment heads value
    elif coin == 2: # if 2
        tails += 1 # increment tails value

    flip_count += 1 # increase flip counter

# at end of while loop
print("Coin has been flipped 100 times!")
print("\tNumber of heads: " + str(heads))
print("\tNumber of tails: " + str(tails))

input("\nPress enter to exit.")
