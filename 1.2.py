# Create a dictionary
student = {
   'name': 'John',
   'age': 22,
   'major': 'Computer Science'
}

# Accessing a value
print(student['name'])

# Adding a new key-value pair
student['grade'] = 'A'

# Modifying an existing value
student['age'] = 23

# Deleting a key-value pair
del student['major']
print(student)

# Create a dictionary
fruits = {'apple': 3, 'banana': 5, 'orange': 2}

# Iterating over keys
for fruit in fruits:
   print(fruit)

# Iterating over values
for count in fruits.values():
   print(count)

# Iterating over key-value pairs
for fruit, count in fruits.items():
   print(f"The count of {fruit} is {count}")

# Create a dictionary
person = {'name': 'Alice', 'age': 30}

# Check if a key exists
if 'name' in person:
   print("Name is present in the dictionary.")
else:
   print("Name is not present.")