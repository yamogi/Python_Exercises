# ch02_ex02.py
#
# Write a program that allows a user to enter his or her two favorite foods.
# The program should then print out the name of a new food by joining the
# original food names together.
#

print("Hi there!")
food_1=input("Please enter one of your favourite foods: ")
print("Great.")
food_2=input("Please enter another one of your favourite foods: ")

print("...")

print("Your new favourite food is: " + food_1 + food_2) # string concatenation

input("\nPress enter to exit.")
