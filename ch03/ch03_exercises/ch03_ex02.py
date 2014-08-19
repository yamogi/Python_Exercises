# Write a program that flips a coin 100 times and then
# tells you the number of heads and tails.

import random # import the random module

# initialising values
flip_count = 0
coin = 0
heads = 0
tails = 0

while flip_count < 100:
    coin = random.randint(1, 2)

    if coin == 1:
        heads += 1
    elif coin == 2:
        tails += 1

    flip_count += 1

print("Coin has been flipped 100 times!")
print("\tNumber of heads: " + str(heads))
print("\tNumber of tails: " + str(tails))

input("\nPress enter to exit.")