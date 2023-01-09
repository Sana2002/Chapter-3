# Initialize a list of dinner guests
dinner_guests = ['Sara', 'Ahmed', 'afrah']

# Print an invitation to each guest in the list
for guest in dinner_guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")

# Print a blank line
print()

# Inform the guests that Ahmed will not be attending
print("Unfortunately, Ahmed is unable to make it to the dinner.")

# Replace Marie Curie with Isaac Newton in the list of guests
dinner_guests[1] = 'Maryam'

# Print an updated invitation to each guest in the list
for guest in dinner_guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")