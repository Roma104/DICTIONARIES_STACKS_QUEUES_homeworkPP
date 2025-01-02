phone_book = {
   'John': '555-1234',
   'David': '555-5678',
   'Bob': '555-8765',
   'Charlie': '555-4321',
   'Diana': '555-9876',
   'Eve': '555-6543',
   'Frank': '555-3456',
   'Grace': '555-7890',
   'Hank': '555-1111',
   'Ivy': '555-2222',
   'Jack': '555-3333',
   'Daniel': '555-4444',
   'Liam': '555-5555',
   'Mia': '555-6666',
   'Nina': '555-7777',
   'Oscar': '555-8888',
   'Paul': '555-9999',
   'Dominic': '555-1010',
   'Rachel': '555-2020',
   'Sam': '555-3030'
}

# Print header
print(f"{'Name':<10} {'Phone Number':<12}")

# Iterate through the phone book
for name, phone in phone_book.items():
    # Check if the name starts with 'D'
    #if name.startswith('D'): ##There's existing function for that :O lol
        #print(f"{name:<10} {phone:<12}")

    # Check if the first letter of the name is 'D'
    if len(name) > 0 and name[0] == 'D':  # Ensure the name has at least one character
        print(f"{name:<10} {phone:<12}")