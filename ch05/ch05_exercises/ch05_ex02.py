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

for i in range(loop_max):
    print("Attribute", str(i+1), "is currently:\t", attribute_values[i])

print()

choice = None

while choice != 0:
    print("Menu:")
    print("0) Exit")
    print("1) Add a point")
    print("2) Remove a point")

    choice = int(input())

    if choice == 0:
        print("Goodbye.")
    elif choice == 1:
        if points_left > 0:
            print("  Add a point to which attribute?")
            print("  1) str")
            print("  2) hp")
            print("  3) wis")
            print("  4) dex")
        
            add_choice = int(input())

            attribute_values[add_choice - 1] += 1
            points_left -= 1

            print()

            print("You have", points_left, "points remaining.")

            for i in range(loop_max):
                print("Attribute", str(i+1),
                "is currently:", attribute_values[i])

            print()

        else:
            print()
            print("No points remaining to distribute!")
            print()

    elif choice == 2:
        if points_left < MAX_POINTS:
            print("  Remove a point from which attribute?")
            print("  1) str")
            print("  2) hp")
            print("  3) wis")
            print("  4) dex")

            rem_choice = int(input())

            if attribute_values[rem_choice -1] > 0:
                attribute_values[rem_choice - 1] -= 1
                points_left += 1

                print()

                print("You have", points_left, "points remaining.")

                for i in range(loop_max):
                    print("Attribute", str(i+1),
                    "is currently:", attribute_values[i])

                print()

            else:
                print()
                print("Attribute cannot fall below zero!")
                print()

        else:
            print()
            print("Hit max points!!")
            print()

    else:
        print("Wat.")
        print()
