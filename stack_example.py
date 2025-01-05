import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""

print("\nand here we start my changes(Nie chaiałem usuwać poprzednich elementów, więc po prostu dodałam reszte dalej heh )\n")

# Create a stack
stack = queue.LifoQueue()

# Put elements on the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)


# Sum the last two numbers of the stack
last = stack.get()  # Remove the last element (8)
second_last = stack.get()  # Remove the second last element (9)
sum_last_two = last + second_last
print("Sum of the last two numbers:", sum_last_two)

# Add the second last element back to the stack (so it's still available for further operations)
stack.put(second_last)

# Calculate the sum of the remaining stack elements
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print("Sum of the remaining stack elements:", remaining_sum)