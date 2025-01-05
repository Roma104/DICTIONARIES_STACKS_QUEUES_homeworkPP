import json

# Open the JSON file in read mode
with open('dogs.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    dogs = json.load(file)

# Print information about dogs younger than 5 years
for dog in dogs:
    if dog['age'] < 5:
        print(f"Name: {dog['name']}")
        print(f"Breed: {dog['breed']}")
        print(f"Age: {dog['age']}")
        print(f"Weight: {dog['weight_kg']} kg")
        print(f"Owner: {dog['owner']}")
        print(f"Vaccinated: {'Yes' if dog['vaccinated'] else 'No'}")
        print()  # Add a blank line between dogs
