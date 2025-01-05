def reverse_string_with_stack(input_string):
    # Initialize an empty stack
    stack = []
    
    # Push each character of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop characters from the stack to form the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Program to reverse user input
text = input("Enter the text to reverse: ")
reversed_text = reverse_string_with_stack(text)
print("Reversed text:", reversed_text)
