# Tuple Concatenation
# Demonstrates tuple concatenation

# initialise inventory values
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print inventory with for loop
print("Your inventory consists of:")
for item in inventory:
    print("\t", item)

# wait for user input
input("\nPress enter to continue.")

# initialise chest values
chest = ("gold", "gems")

# print chest with for loop
print("You have found a chest!")
print("The chest contains:")
for item in chest:
    print("\t", item)

# wait for user input
input("\nPress enter to continue.")

# concatenating the inventory and chest tuples
print("You add the contents of the chest to your inventory:")
inventory += chest # <-- CONCATENATION OCCURS HERE
# printing the new inventory with for loop
print("Your inventory now consists of:")
for item in inventory:
    print("\t", item)
