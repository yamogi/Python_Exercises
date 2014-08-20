# No Vowels
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ") # user enters a message
new_message = "" # initialise empty string for new message
VOWELS = "aeiou" # this is a constant, holding possible vowels

print() # extra newline
for letter in message: # iterate through every letter in user's message
    if letter.lower() not in VOWELS: # if letter is not a vowel
        new_message += letter # append it to the new message
        # then show the updated message
        print("A new string has been created:", new_message)

print("\nYour message with vowels is:", new_message) # finish
