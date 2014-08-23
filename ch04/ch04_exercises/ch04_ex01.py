# ch04_ex01.py
#
# Write a program that counts for the user. Let the user enter the starting
# number, ending number, and the amount by which to count.
#

print("Hello there!")
print("This is the counting program")

# obtain start, end, and count values
start = int(input("Please enter the number to start counting from: "))
end = int(input("Please enter the number to count to: "))
count = int(input("Please enter the amount by which to count: "))

print("Great! Here is your counting:")
# note (end+1) instead of just end
# otherwise counting ends before it hits the end value
for i in range(start, (end+1), count):
    print(i, end=" ")

print() # extra newline
