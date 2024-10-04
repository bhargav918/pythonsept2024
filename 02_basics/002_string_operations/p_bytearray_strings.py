#!/use/bin/python3
"""
Purpose: bytearray strings
"""
ordinary_string = "Tomorrow will be ours!!"
print("ordinary_string   :",ordinary_string)
print("type(ordinary_string):", type(ordinary_string))

print("ordinary_string[9] " ,ordinary_string[9])
print("ordinary_string[9:17] :",ordinary_string[9:17])
print(ordinary_string.find("will be"))


#ordinary strings are immutable
#byte array strings are mutable



print()
#ord and #char
#ASCII 0->111
print("chr(111):", chr(111))
print("ord('o'):", ord('o'))
