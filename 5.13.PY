def calculate_rpn():
    stack = []
    while True:
        token = input("Enter a number, operator (+, -, *, /), or '=' to calculate: ").strip()
        
        if token.isdigit():  # If the token is a number
            stack.append(float(token))
        elif token in "+-*/":  # If the token is an operator
            if len(stack) < 2:
                print("Error: Not enough operands on the stack for the operation.")
                continue
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand
            
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                if b == 0:
                    print("Error: Division by zero is not allowed.")
                    stack.append(a)  # Push operands back onto the stack
                    stack.append(b)
                    continue
                result = a / b
            
            stack.append(result)  # Push the result back onto the stack
        elif token == "=":  # If the token is the equal sign
            if len(stack) != 1:
                print("Error: Stack should contain only one item (the result).")
            else:
                print("Result:", stack.pop())
            break
        else:
            print("Invalid input. Please enter a number, an operator, or '='.")

# Example RPN calculations
print("Calculate RPN expressions:")
print("Example inputs: 2, 3, +, =")
calculate_rpn()
