store_inventory = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

# Print the list of products and their quantities
print("Product List:")
for product, quantity in store_inventory.items():
    print(f"{product:<20} {quantity}")

# Calculate the total number of products in the store
total_products = sum(store_inventory.values())

# Print the total
print("\nTotal number of products in the store:", total_products)