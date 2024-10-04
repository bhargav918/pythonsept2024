"""
Purpose: To check largest of give two numbers
"""

letter = input("Enter any character:").strip()


if letter in "aeiou":
    print(f"{letter} is a LOWER VOWEL CHARACTER")
elif letter in "AEIOU":
    print(f"{letter} is a UPPER VOWEL CHARACTER")
else:
    print(f"{letter} may be a CONSONANT")
