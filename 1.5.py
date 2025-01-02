countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":84480000},
{"name":"Japan", "population":124500000},
{"name":"Norway", "population":5520000},
{"name":"China", "population":1411000000},
]

# Print header
print(f"{'COUNTRY':<10} {'POPULATION':<12}")

# Iterate through the list and print each country's data
## <10 and <12 mean the text is left-aligned in a column of width 10 and 12, respectively.
for country in countries:
    print(f"{country['name']:<10} {country['population']:<12}")