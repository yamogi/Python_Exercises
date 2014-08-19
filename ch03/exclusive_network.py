# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username: # obtain a username
    username = input("Username: ")

password = ""
while not password: # obtain a password
    password = input("Password: ")

print("\n\t", end="") # extra newline and tab

if username == "M.Dawson" and password == "secret":
    print("Hi, Mike.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Hey, Sid.")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("What's up, Shigeru?")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it, Will?")
    security = 3
elif username == "guest" or password == "guest": # note the "or"
    print("Welcome, guest.")
    security = 1
else: # if all else fails, lock the user out
    print("Login failed. You're not so exclusive.\n")

input("\nPress enter to exit.")
