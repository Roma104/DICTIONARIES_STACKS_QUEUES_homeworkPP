import queue

def decimal_to_binary(number):
    stack = queue.LifoQueue()  # Create a stack
    original_number = number  # Save the original number for display

    # Convert the number to binary using repeated division by 2
    while number > 0:
        remainder = number % 2
        stack.put(remainder)  # Push remainder onto the stack
        number = number // 2  # Update the number by dividing it by 2

    # Pop and display all values from the stack to get the binary number
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())

    # Display results
    print(f"Natural number: {original_number}")
    print(f"Binary number: {binary_number}")

# Example usage
decimal_to_binary(18)
