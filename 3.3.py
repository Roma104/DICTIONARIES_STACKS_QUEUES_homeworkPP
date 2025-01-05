import queue

# Expressions to check
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = []  # Use a list as a stack
    brackets = {')': '(', '}': '{', ']': '['}  # Closing to opening bracket mapping
    
    for char in expression:
        if char in '({[':  # If it's an opening bracket
            stack.append(char)
        elif char in ')}]':  # If it's a closing bracket
            if not stack or stack.pop() != brackets[char]:  # Check for matching opening bracket
                return False

    return len(stack) == 0  # True if stack is empty (all brackets matched)

# Checking each expression
if brackets_ok(expression1):
    print("Expression 1: Brackets are correct.")
else:
    print("Expression 1: Brackets are not correct.")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct.")
else:
    print("Expression 2: Brackets are not correct.")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct.")
else:
    print("Expression 3: Brackets are not correct.")
