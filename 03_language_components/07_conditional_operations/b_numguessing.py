#!/usr/bin/python3
"""
Purpose: Number Guessing Game
"""
LUCKY_NUMBER = 69

guessed_number = int(input("Enter a number, between 0 & 100 inclusive:"))



# print(f"{LUCKY_NUMBER                   =}")
print(f"{guessed_number                 =}")

#another method
if guessed_number == LUCKY_NUMBER:
    print("YOU GUESSED CORRECTLY !!!")
elif guessed_number > LUCKY_NUMBER:  # 78 > 69
    print("Please Try Again with reducing your guess number")
elif guessed_number < LUCKY_NUMBER:  # 34 < 69
    print("Please Try Again with increasing your guess number")