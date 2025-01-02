price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

# Print the list of products and their prices before the discount
print("Prices Before Discount:")
for product, price in price_list.items():
    print(f"{product:<10} ${price:.2f}")

# Calculate the total value of products before the discount
total_before_discount = sum(price_list.values())
print("\nTotal value before discount: $", round(total_before_discount, 2))

# Apply a 10% discount and update the price list
discount_rate = 0.10
for product in price_list:
    price_list[product] = round(price_list[product] * (1 - discount_rate), 2)

# Print the list of products and their prices after the discount
print("\nPrices After Discount:")
for product, price in price_list.items():
    print(f"{product:<10} ${price:.2f}")

# Calculate the total value of products after the discount
total_after_discount = sum(price_list.values())
print("\nTotal value after discount: $", round(total_after_discount, 2))