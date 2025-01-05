import json

# Load reservation data from JSON file
def load_reservation_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Calculate the summary of reservations
def calculate_summary(data):
    total_rooms = len(data["reservations"])
    paid_reservations = sum(1 for res in data["reservations"] if res["paid"])
    unpaid_reservations = total_rooms - paid_reservations
    total_paid_value = sum(res["nights"] * res["price_per_night"] for res in data["reservations"] if res["paid"])
    total_unpaid_value = sum(res["nights"] * res["price_per_night"] for res in data["reservations"] if not res["paid"])
    
    return {
        "total_rooms": total_rooms,
        "paid_reservations": paid_reservations,
        "unpaid_reservations": unpaid_reservations,
        "total_paid_value": total_paid_value,
        "total_unpaid_value": total_unpaid_value
    }

# Print the summary of reservations
def print_reservation_summary(file_path):
    reservations_data = load_reservation_data(file_path)
    summary = calculate_summary(reservations_data)
    
    print(f"Number of rooms: {summary['total_rooms']}")
    print(f"Number of paid reservations: {summary['paid_reservations']}")
    print(f"Number of unpaid reservations: {summary['unpaid_reservations']}")
    print(f"Total value of paid reservations: ${summary['total_paid_value']:.2f}")
    print(f"Total value of unpaid reservations: ${summary['total_unpaid_value']:.2f}")

# Specify the path to the reservations.json file
file_path = 'reservations.json'

# Print the reservation summary
print_reservation_summary(file_path)
