import json

def display_exchange_rates(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Print the table header
    print("Date            Buying Rate     Selling Rate")
    print("============================================")
    
    # Iterate over the rates and print each one
    for rate in data["rates"]:
        date = rate["effectiveDate"]
        buy_rate = rate["bid"]
        sell_rate = rate["ask"]
        print(f"{date}      {buy_rate:.4f}          {sell_rate:.4f}")

# Display data from euro.json
display_exchange_rates("euro.json")
