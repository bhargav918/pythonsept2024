#!/usr/bin/python3

print("" % ())   #old style
print("{}".format(""))  # new style
print(f'{""}')
print()


print("Hello{name}".format(name = "world"))

name = "world"
print(f"hello {name}")

number = 12345
print(f"number is {number}")