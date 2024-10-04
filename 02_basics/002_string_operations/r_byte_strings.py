#!/usr/bin/python3


my_string = "python is interesting"
# string with encoding utf-8
b_string = bytes(my_string, "utf-8")
print(b_string, type(b_string))

#bytes to string
print(b"hello".decode("utf-8"))