#!/usr/bin/python3

"""
purpose: range function
        - bult-in function
        - used for sequence generation
        - SYNTAX
            range(initial_value,final_value,step)
        - Defaults
            initial_value=0
            STEP=+1
        - Final value is mandatory
        - To get the values
            - either convet to any iterable
            or, for loop for that object
        - Lazy loading object

        """

values = range(9)
print(type(values), values)

values = range(10)
print(type(values), values)

values = range(0,9,2)
print(list(values), values)

values = range(0,9-1)
print(list(values), values)

values = range(9,-1,-1)
print(list(values), values)

values = range(9,-1,-3)
print(list(values), values)
