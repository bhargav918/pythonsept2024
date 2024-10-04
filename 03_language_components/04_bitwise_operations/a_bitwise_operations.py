#!/usr/bin/python3

"""
purpose: Bitwise operations




& binary AND
| BINARY OR
^ BINARY XOR      #if total count of 1's is odd ,it result in 1 else 0
~ BINARY 1'S COMPLIMENT
<<   BINARY SHIFT LEFT
>>   BINARY SHIFT RIGHT

"""

num1 = 60
num2 = 13

print("num1=",num1, bin(num1))
print("num2=",num2, bin(num2))

num3 = num1 & num2
print("Line 1 - value of num3 is ", num3)

num3 = num1 | num2
print("Line 1 - value of num3 is ", num3)

num3 = num1 ^ num2
print("Line 1 - value of num3 is ", num3)

num3 = num1 << num2
print("Line 1 - value of num3 is ", num3)

num3 = num1 >> num2
print("Line 1 - value of num3 is ", num3)