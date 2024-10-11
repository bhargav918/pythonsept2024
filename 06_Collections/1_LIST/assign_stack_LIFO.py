"""
 Assignment
            ----------
            1) implement the stack mechanism - LIFO
            Take the values in run time
            1. push   - add an element
            2. pop    - delete last element
            3. status - stack size
"""


list = []  

# Push operation
items = input("Enter items to push onto the stack : ")
for item in items.split():  # Split the input string by spaces
    list.append(item)  # Add each item to the stack
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

#o/p
# Enter items to push onto the stack : 1 2 3
# Stack after push: ['1', '2', '3']
# Popped item: 3
# Stack size: 2
# Exiting.