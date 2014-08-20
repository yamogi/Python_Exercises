# Hero Inventory 2.0
# Demonstrates tuples

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print with a for loop
print("Your items:")
for item in inventory:
    print(item)

# wait for user input

# get the length of the tuple
#  - note that "healing potion" is counted as a single
#    element, even though it consists of two words
print("You have", len(inventory), "items in your possession.")

# wait for user input
input("\nPress enter to continue")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# display one item through an index
index = int(input("\nEnter the index number for an item in the inventory: "))
print("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])
