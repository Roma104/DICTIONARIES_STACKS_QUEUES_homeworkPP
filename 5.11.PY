import json

# Defining the file name for the voting data
file_name = "voting.json"

# Read the contents of the JSON file, or initialize an empty dictionary if the file doesn't exist
try:
    with open(file_name, "r") as file:
        voting_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    voting_data = {}  # Create an empty dictionary if the file is missing or corrupted


person_name = input("Name of the person you are voting for: ").strip()

# Update the vote count for the person
if person_name in voting_data:
    voting_data[person_name] += 1  # Increment the vote count
else:
    voting_data[person_name] = 1  # Add the person with an initial vote count of 1

# Save the updated voting data back to the JSON file
with open(file_name, "w") as file:
    json.dump(voting_data, file, indent=4)

print(f"Vote recorded for {person_name}. Current votes: {voting_data[person_name]}")