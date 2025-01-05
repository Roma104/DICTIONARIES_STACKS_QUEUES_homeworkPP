import json

# Define a dictionary for the favorite book or movie
favorite = {
    "title": "Zatracenie",
    "author_or_director": "Osamu Dazai",
    "genre": "Powieść",
    "year": 1948,
    "rating": 10
}

# Write the dictionary to a JSON file
def write_to_json_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Specify the output JSON file
file_path = "favourite.json"

# Write the favorite data to the JSON file
write_to_json_file(favorite, file_path)

print(f"Favorite data written to {file_path} successfully!")
