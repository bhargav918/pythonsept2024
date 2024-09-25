#!/usr/bin/python3

"""
identifiers- keywords defined by the user

"""


#Loading a module 
import keyword

print(keyword.kwlist)
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(True)

my_value = "something"
print(my_value)  #Identifier

print(keyword.iskeyword("True"))
print(keyword.iskeyword("true"))
print(keyword.iskeyword("my_value"))

# variable -> public variable
# _variable -> protected variable  
# __variable-> private variable
# _variable_  -> Builtin function eg; _init_ , _doc_, _name_