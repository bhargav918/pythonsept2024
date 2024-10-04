#!/usr/bin/python3

"""
purpose: bool() function usage


"""

name = "Bhargav"
print("bool(name)   =",bool(name))
print("bool(name !='')    =",bool(name !=''))

#explicit function

num1 = -0.0000056
if num1 != 0:
    print("It is not zero")

#implicit function
if num1:
    print("It is not zero")

if 1:
    print("It will print everytime")

if 0:
    print("It will not print everytime")