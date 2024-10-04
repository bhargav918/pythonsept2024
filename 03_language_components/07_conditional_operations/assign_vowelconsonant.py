#!/usr/bin/python3

char = input("Enter a character: ").lower()  # to convert capital letter to small

if char in 'aeiou':
    print(char, "is a Vowel")
else:
    print(char, "is a Consonant")