# Three-Year-Old Simulator
# Demonstrates the while loop

print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")

response = ""
# Ensure to run this while loop using python3.x, not python2.x
# Or else errors occur
while response != "Because.":
    response = input(" - Why?\n")

print(" - Oh. Okay.")

input("\nPress enter to exit.")
