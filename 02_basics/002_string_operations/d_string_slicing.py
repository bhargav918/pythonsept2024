#!/usr/bin/python3

"""
purpose: string operations
            indexing
"""

language = 'python programming'
print("language :" ,language)

# p y t h o n p r o g r  a  m  m  i  n  g

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16.....> forward indexing
#                           -5 -4 -3 -2 -1 ----> reverse indexing

#()--function call
#[]--indexing

#indexing
print("language[0]   :", language[0])
print()

#slicing
# Slicing
print("String Slicing")
print ("language [0:11] : ", language [0:11])          
print ("language [5:17]: ", language [5:17])
print ("language [7:10] :", language[7:10])


# String Slicing
# language [0:11] :  python prog
# language [5:17]:  n programmin
# language [7:10] : pro

# NoteL: In python it doesn't include the last value in a boundary condition

print()
print ("language [0:5] : ", language [0:5])   #pytho
print ("language [0:6] : ", language [0:6])   #python


print()
print ("language [7:18] : ", language [7:18])   #pytho
print ("language [7:999] : ", language [7:999])