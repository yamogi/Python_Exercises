# Geek Translator
# Demonstrates using dictionaries

# dictionary = {"key1": "value1",
#               "key2": "value2"}
geek = {"404": "clueless.",
        "Googling": "searching using Google",
        "Keyboard Plaque": "the collection of debris",
        "Link Rot": "the process by which web page links become obsolete",
        "Percussive Maintenance": "creative problem solving",
        "Uninstalled": "being fired"}

choice = None

while choice != "0":
    print(
            """
            GEEK TRANSLATOR

            0 - Quit
            1 - Look Up a Geek Term
            2 - Add a Geek Term
            3 - Redefine a Geek Term
            4 - Delete a Geek Term
            """
    )

    choice = input("Choice: ")
    print()

    if choice == "0":   # quit
        print("Goodbye.")
    elif choice == "1": # define term
        term = input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)
    elif choice == "2": # add term
        term = input("What term do you want me to add?: ")
        if term not in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("That term already exists! Try redefining it (3).")
    elif choice == "3": # redefine term
        term = input("What term do you want me to redefine?: ")
        if term in geek:
            definition = input("What's the new definition?: ")
            geek[term] = definition
            print("\n", term, "has been redefined.")
        else:
            print("\nThat term doesn't exist! Try adding it (2).")
    elif choice == "4": # delete term
        term = input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print("\nOkay, I deleted", term)
        else:
            print("\nI can't do that!")
            print("\n", term, "does not exist in the dictionary.")
    else: #default fail condition
        print("Sorry, but \"", choice, "\" is not a valid choice.")
