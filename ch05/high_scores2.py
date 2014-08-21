# High Scores 2.0
# Demonstrates nested sequences

scores = [] # empty list

choice = None # default init

while choice != "0":
    print(
            """
                High Scores 2.0

                0 - Quit
                1 - List Scores
                2 - Add a Score
            """
        )

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Goodbye.")
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = score, name         # create a tuple
        scores.append(entry)        # add the high score to the list
        scores.sort(reverse=True)   # sort list by highest first
        scores = scores[:5]         # keep only the top 5 scores
    else:
        print("Sorry, \"", choice, "\" is not a valid choice.")
