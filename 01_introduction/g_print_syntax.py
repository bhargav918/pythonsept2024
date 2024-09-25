#!/usr/bin/python3
"""
Escape sequences
    - characters whose presence is felt but they were not printed
    \t - tab space
    \n - new line
    \b - overwrite previous character

    r'' - raw string

"""

print("Hello world python")
print("Hello \tworld \tpython")
print("Hello \tworld \npython")

#To ignore the escape sequence

print("Hello \tworld \\npython") 
print(r"Hello \tworld \npython")

print("hello" , end="\n")
print("world" , end="\n")

print("hello" , end="__")
print("world")

print("hello" , end="\t")
print("world")

print("hello" , "python", 1234, end="\t") #default sep=' '
print("world")

print("hello" , "python", 1234, end="\t", sep=";") #default sep=' '
print("world") #default end='\n'

# \b Overwrites previous character

print("he\bi")
print("12\b34")
print("first\bsecond")
print("\bsecond")
print("second\b")
print("second\b12")


# Unicode characters   \uxxx - iunicode character

print("\u2089")
print("\u018e")

# \x...   - hexadecimal number
print("\x24")
print("\xf1")
print()
