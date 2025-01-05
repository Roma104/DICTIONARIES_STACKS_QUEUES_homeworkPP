# Basic data dictionary
basic_data = {
   "name": "Barbara",
   "age": 21
}

# Advanced data dictionary
advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Combine both dictionaries into the 'person' dictionary
person = {**basic_data, **advanced_data}

# Print the contents of the 'person' dictionary
print(person)
