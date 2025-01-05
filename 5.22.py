import json

# Create an empty dictionary to store product data
product = {}

# Read product data from the keyboard
product["name"] = input("Enter the product name: ").strip()
product["price"] = float(input("Enter the product price (e.g., 19.99): "))
paid_input = input("Has the product been paid for? (yes/no): ").strip().lower()

# Convert 'yes'/'no' input to a boolean value
if paid_input == "yes":
    product["paid"] = True
elif paid_input == "no":
    product["paid"] = False
else:
    print("Invalid input for 'paid'. Please enter 'yes' or 'no'.")
    exit()  # Exit the program if the input is invalid

# Save product data to JSON file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4)

print("Product data saved to 'product.json'!")
