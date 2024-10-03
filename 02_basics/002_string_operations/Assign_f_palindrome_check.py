#!/usr/bin/python3

"""

purpose: demonstartion of palindrome
    palindrome check
        mom
        dad

Algorithm:
-------------

step-1: take the string in run-time and store in a variable

"""

pali1 = str(input("Enter a string :"))

pali2 = pali1[::-1]    # reversing the string using slicing

if pali1 == pali2:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")

    
