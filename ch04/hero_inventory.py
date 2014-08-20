# Hero Inventory
# Demonstrates tuple creation

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

# wait for user input
input("\nPress enter to continue.")

#create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple
print("\nThe tuple inventory is:")
print(inventory)

# print each element in the tuple
print("\nYour items:")
for item in inventory:
    print("\t", item)
