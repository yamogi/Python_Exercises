# Maitre D'
# Demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("\t How many dollars do you slip the maitre D'? "))

print()

if money: # if any money at all
    print("Ah, I am reminded of a table. Right this way.") # money == true
else: # if zero (0) money is given
    print("Please sit. It may be a while.") # money == false

input("\n\nPress enter to exit.")
