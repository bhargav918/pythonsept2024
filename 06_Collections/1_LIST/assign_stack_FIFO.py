
"""

2) implement the queue mechanism - FIFO
            Take the values in run time
            1. push   - add an element
            2. pop    - delete last element
            3. status - queue size
                --------
            ->         ->
                --------
            HINT: list.insert(), list.pop(), len()
"""




list = []  

# Push operation
items = input("Enter items to push onto the stack : ")
for item in items.split():  # Split the input string by spaces
    list.insert(0,item)  # Add each item to the stack
print(f"Stack after push: {list}")

# Pop operation
if len(list) > 0:
    popped_item = list.pop()
    print(f"Popped item: {popped_item}")
else:
    print("Stack is empty.")

# Status operation
print(f"Stack size: {len(list)}")

# Exit message
print("Exiting.")

#o/p:
# Enter items to push onto the stack : 1 2 3
# Stack after push: ['3', '2', '1']
# Popped item: 1
# Stack size: 2
# Exiting.