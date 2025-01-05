import csv

# Step 1: Read provinces from 'province.csv' with the correct encoding
province_dict = {}
with open('province.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        province_dict[row[0]] = row[1]  # Key: letter, Value: province name

# Step 2: Initialize a dictionary to count the vehicles for each province
vehicle_count = {key: 0 for key in province_dict.keys()}  # Initialize count for each province

# Step 3: Read vehicle registration numbers from 'vehicle.txt' and count vehicles for each province
with open('vehicle.txt', mode='r') as file:
    for line in file:
        registration_number = line.strip()  # Remove any extra whitespace or newline characters
        first_letter = registration_number[0]  # Get the first letter of the registration number

        # Step 4: Check if the first letter matches a province letter
        if first_letter in vehicle_count:
            vehicle_count[first_letter] += 1  # Increment the count for that province

# Step 5: Print the results
for letter, count in vehicle_count.items():
    print(f"Province {province_dict[letter]}: {count} vehicles")
