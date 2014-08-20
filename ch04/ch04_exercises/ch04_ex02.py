# Create a program that gets a message from the user and
# then prints it out backwards

print("Hello!")
print("I will reverse any message you input.")

print("Please enter a message:")
message = input() # obtain user input

message_length = len(message) # get message length

print("\nYour reversed message is:\n\t", end="")
# start at the last index, work towards 0, -1 each time
for i in range((message_length - 1), -1, -1):
    print(message[i], end="")

print() # extra newline
