
import os
print(os.path.sep)  
os.path.sep = '-'
filename = 'file.txt'
root, ext = os.path.splitext(filename)

print(root)  
print(ext)  