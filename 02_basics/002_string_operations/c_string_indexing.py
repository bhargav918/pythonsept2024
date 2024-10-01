#!/usr/bin/python3

"""
purpose: string operations
            indexing
"""

language = 'python programming'
print(language, type(language))

#len() to get the number of  characters in a string


language = 'python programming'
print("len(language)", len(language))

#Note : indexing starts from 0

# p y t h o n p r o g r  a  m  m  i  n  g

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16.....> forward indexing
#                           -5 -4 -3 -2 -1 ----> reverse indexing

#()--function call
#[]--indexing

print("language   :", language)
print("language[14]:", language[14])
print("language[6]:", language[6])
print("language[17]:", language[17])

print()
print("language[0]  :", language[0])
print("language[-0]  :", language[-0])

print()
print("language[-18]  :", language[-18])
print("language[0]  :", language[0])