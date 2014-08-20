# Pizza Slicer
# Demonstrates string slicing

word = "pizza" # initialise word value

print( # give overview of string index
      """
         Slicing "Cheat Sheet"

     0    1     2     3     4     5
     -----------------------------
    |  p  |  i  |  z  |  z  |  a  |
     -----------------------------
   -5    -4    -3    -2    -1

      """
)

print("Enter the beginning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")

start = None

while start != "": # if start is NOT empty
    start = (input("\nStart: "))

    if start: # if user does not simply press enter

        start = int(start) # no need to gain input if start is not empty
        finish = int(input("Finish: "))

        print("word[", start, ":", finish, "] is", end=" ")
        print(word[start:finish]) # print word according to indices
