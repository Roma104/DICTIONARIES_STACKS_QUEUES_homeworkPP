from collections import deque

def customer_service():
    queue = deque()
    ticket_number = 1

    while True:
        print("\nCustomer Service System")
        print("1. Add a new customer")
        print("2. Serve the next customer")
        print("3. Show the queue")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            # Add a new customer to the queue
            queue.append(ticket_number)
            print(f"Customer with ticket #{ticket_number} added to the queue.")
            ticket_number += 1
        elif choice == "2":
            # Serve the next customer
            if queue:
                next_customer = queue.popleft()
                print(f"Serving customer with ticket #{next_customer}.")
            else:
                print("No customers in the queue to serve.")
        elif choice == "3":
            # Display the queue
            if queue:
                print(f"Current queue: {list(queue)}")
            else:
                print("The queue is empty.")
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the customer service system
customer_service()
