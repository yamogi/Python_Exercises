# Write a Tipper program where the user enters a
# restaurant bill total. The program should then
# display two amounts: a 15 percent tip and a 20
# percent tip.

print("Hi there!")
total=float(input("How much was your meal today?\n   "))

print("Calculating tips...")

tip_15 = total * 0.15
tip_20 = total * 0.2

# At this point I am unable to work out how
# to do the correct number of decimal places.
print("A 15% tip would be: " + str(tip_15))
print("A 20% tip would be: " + str(tip_20))

input("\nPress enter to exit.")
