# ch05_ex02.py
#
# Write a Character Creator program for a role-playing game. The player should
# be given a pool of 30 points to spend on four attributes: Strength, Health,
# Wisdom, and Dexterity. The player should be able to spend points from the
# pool on any attribute and should also be able to take points from an
# attribute and put them back in the pool.
#

MAX_POINTS = 30 # max number of points allowed to be distributed
points_left = 30 # points remaining
#attribute_names = ("strength",
#                   "health",
#                   "wisdom",
#                   "dexterity") # empty attributes tuple (not required)
attribute_values = [0,0,0,0] # empty attributes list
loop_max = 4 # setting i values

print("Greetings, adventurer!")
print("The time has come to allocate your resources!")

print("You have", points_left, "points remaining.")

for i in range(loop_max): # go through the attributes and print current values
    print("Attribute", str(i+1), "is currently:", attribute_values[i])

print() # extra newline

choice = None # initialise choice

while choice != 0: # as long as user doesn't intentionally exit
    print("Menu:") # display the menu
    print("0) Exit")
    print("1) Add a point")
    print("2) Remove a point")

    choice = int(input()) # obtain choice

    if choice == 0: # [EXIT]
        print("Goodbye.")
    elif choice == 1: # [ADD]
        if points_left > 0: # if user has points left to spend
            print("  Add a point to which attribute?")
            print("  1) str")
            print("  2) hp")
            print("  3) wis")
            print("  4) dex")
        
            add_choice = int(input()) # choose the attribute

            attribute_values[add_choice - 1] += 1 # increase attr by 1 point
            points_left -= 1 # remove 1 point from remaining point count

            print() # extra newline

            print("You have", points_left, "points remaining.")

            for i in range(loop_max): # print current attribute values
                print("Attribute", str(i+1),
                "is currently:", attribute_values[i])

            print() # extra newline

        else: # if user has no points remaining
            print() # extra newline
            print("No points remaining to distribute!")
            print() # extra newline

    elif choice == 2: # [REMOVE]
        if points_left < MAX_POINTS: # if user has points left to remove
            print("  Remove a point from which attribute?")
            print("  1) str")
            print("  2) hp")
            print("  3) wis")
            print("  4) dex")

            rem_choice = int(input()) # choose the attribute

            if attribute_values[rem_choice -1] > 0: # if attr is zero or above
                attribute_values[rem_choice - 1] -= 1 # decrease attr value
                points_left += 1 # add 1 point to remaining point count

                print() # extra newline

                print("You have", points_left, "points remaining.")

                for i in range(loop_max): # print current attribute values
                    print("Attribute", str(i+1),
                    "is currently:", attribute_values[i])

                print() # extra newline

            else: # if attr is zero, it cannot fall below zero
                print() # extra newline
                print("Attribute cannot fall below zero!")
                print() # extra newline

        else: # if user has no points left to remove (i.e. attrs all zero)
            print() # extra newline
            print("Hit max points!!")
            print() # extra newline

    else: # if user doesn't pick any recognised menu choice
        print("Wat.")
        print() # extra newline
