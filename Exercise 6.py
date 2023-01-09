# Initialize a list of dinner guests
dinner_guests = ['Afrah', 'Ahmed', 'Sara']

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

# Print a blank line
print()

# Inform the guests that the dinner table won't arrive in time and only two people can be invited
print("I'm sorry to inform you that my new dinner table won't arrive in time and I can only invite two people for dinner.")

# Keep removing guests from the list until only two names remain
while len(dinner_guests) > 2:
    # Remove the last guest from the list and store their name in a variable
    sorry_guest = dinner_guests.pop()
    # Print a message to the removed guest letting them know they are no longer invited to dinner
    print("Dear " + sorry_guest + ", I'm sorry to inform you that I am unable to invite you to dinner.")

# Print a message to each of the remaining guests letting them know they are still invited to dinner
for guest in dinner_guests:
    print("Dear " + guest + ", I'm happy to inform you that you are still invited to dinner.")

# Remove the remaining guests from the list
del dinner_guests[0]
del dinner_guests[0]

# Print the updated list to verify that it is now empty
print()
print(dinner_guests)
