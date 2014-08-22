# Quotation Manipulation
# Demonstrates string methods

# Quote from IBM Chairman, Thomas Watson, in 1943
quote = "I think there is a world market for maybe five computers."

print("Original quote:")
print(quote) # displays str value

print("\nIn uppercase:")
print(quote.upper()) # converts to upper

print("\nIn lowercase:")
print(quote.lower()) # converts to lower

print("\nAs a title:")
print(quote.title()) # capitalises first letter of each word

print("\nWith a minor replacement:")
print(quote.replace("five", "millions of")) # replaces first with second

print("\nOriginal quote is still:")
print(quote) # displays str value

input("\n\nPress the enter key to exit.")
