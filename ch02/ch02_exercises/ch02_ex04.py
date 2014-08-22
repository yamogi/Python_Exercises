# ch02_ex04.py
#
# Write a car salesman program where the user enters the base price of a car.
# The program should add on a bunch of extra fees such as tax, license, dealer
# prep, and destination charge. Make tax and license a percent of the base
# price. The other fees should be set values. Display the actual price of the
# car once all the extras are applied.
#

print("Good day sir! Come to buy a car, have we?")
print("Excellent, excellent...")
price = int(input("Please enter the price of the car: "))

print("Hmm... we'll have to do some calculations")

# old formatting (spaces)
"""
tax = price * 0.15 # proportional value
print("   Tax is:                " + str(tax))
license = price * 0.25 # proportional value
print("   License is:            " + str(license))
dealer_prep = 850 # fixed value
print("   Dealer prep is:        " + str(dealer_prep))
dest_charge = 1200 # fixed value
print("   Destination charge is: " + str(dest_charge))
"""

# new formatting (tabs)
tax = price * 0.15 # proportional value
print("\tTax is:\t\t\t" + str(tax))
license = price * 0.25 # proportional value
print("\tLicense:\t\t" + str(license))
dealer_prep = 850 # fixed value
print("\tDealer prep is:\t\t" + str(dealer_prep))
dest_charge = 1200 # fixed value
print("\tDestination charge is:\t" + str(dest_charge))

price = (price + tax + license + dealer_prep + dest_charge) # total

print("Okay, the new price is:\t\t" + str(price))

input("\nPress enter to exit.")
