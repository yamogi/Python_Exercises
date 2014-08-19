# Finicky Counter
# Demonstrates the break and continue statements

count = 0
while True: # technically this is an infinite loop
    count += 1
    if count > 10:
        break    # end inf loop if count greater than 10
    if count == 5:
        continue # skip 5 (jump to top of the loop)
    print(count)

input("\nPress enter to exit.")
