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
strength  = 0 # hero's current str value
health    = 0 # hero's current health value
wisdom    = 0 # hero's current wisdom value
dexterity = 0 # hero's current dex value

print("Greetings, adventurer!")
print("The time has come to allocate your resources!")

print("You have", points_left, "points remaining.")
