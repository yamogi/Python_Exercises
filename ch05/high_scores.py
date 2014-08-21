# High Scores
# Demonstrates list methods

scores = [] # empty list

choice = None # default init

# DISPLAYING THE MENU
while choice != "0":
    print(
    """
	High Scores

	0 - Exit
	1 - Show Scores
	2 - Add a Score
	3 - Delete a Score
	4 - Sort Scores
    """
    )

    choice = input("\tChoice: ")
    print()

    if choice == "0":
        print("Goodbye.") # exit
    elif choice == "1":
        print("==================================")
        print("High Scores")
        for score in scores:
            print("\t", score) # display scores
        print("==================================")
    elif choice == "2":
        score = int(input("Please input a score: "))
        scores.append(score) # add a high score
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score) # remove a high score
        else:
            print(score, "isn't in the high scores list.")
    elif choice == "4":
        scores.sort(reverse=True) # sort the scores, largest first
    else: # anything else...
        print("Sorry, but", choice, "is not a valid choice.")
