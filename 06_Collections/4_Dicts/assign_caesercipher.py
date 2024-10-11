# Assignment
# chr(), ord()
# print("chr(77) ", chr(77))
# print("ord('M')", ord("M"))
# caesar cipher
# a b c d e f ......
# 0 1 2 3 4 5 .......
# +3
# bad -> edg
# ex: attack is planned to happen on next sunday

# HINT : % operation, chr(), ord(), list comprehension
# chr(77)  M
# ord('M') 77


# Original text and shift value
text = "attack is planned to happen on next sunday"
shift = 3

# Caesar cipher using list comprehension
Caesar_cipher = [
    chr((ord(char) - ord('a') + shift) % 26 + ord('a'))  # For lowercase letters
    if 'a' <= char <= 'z' else
    chr((ord(char) - ord('A') + shift) % 26 + ord('A'))  # For uppercase letters
    if 'A' <= char <= 'Z' else
    char  # Non-alphabetic characters remain unchanged
    for char in text
]

# Join the list into a single string
changed_text = ''.join(Caesar_cipher)

# Output the results
print("Original:", text)
print("Changed:", changed_text)

# Displaying chr and ord examples
print("chr(77):", chr(77))  # Output: M
print("ord('M'):", ord('M'))  # Output: 77

# ord()
# Purpose: Converts a character (string of length 1) to its corresponding integer Unicode code point.
#eg:
# print(chr(65))  # Output: 'A'
# print(chr(97))  # Output: 'a'

# chr()
# Purpose: Converts an integer (representing a Unicode code point) to its corresponding character.

#eg:
# print(ord('A'))  # Output: 65
# print(ord('a'))  # Output: 97
