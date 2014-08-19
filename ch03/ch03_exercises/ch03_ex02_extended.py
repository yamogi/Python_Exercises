# Write a program that flips a coin 100 times and then
# tells you the number of heads and tails.

import random # import the random module

# initialising values
flip_count = 0
coin = 0
heads = 0
tails = 0

total_flips = int(input("Enter the number of times you wish the coin to be flipped: "))

while flip_count < total_flips:
    coin = random.randint(1, 2)

    if coin == 1:
        heads += 1
    elif coin == 2:
        tails += 1

    flip_count += 1

heads_percent = ((heads / total_flips) * 100)
tails_percent = ((tails / total_flips) * 100)

print("Coin has been flipped", total_flips, "times!")
print("\tNumber of heads: " + str(heads) + " (" + str(heads_percent) + "%)")
print("\tNumber of tails: " + str(tails) + " (" + str(tails_percent) + "%)")
