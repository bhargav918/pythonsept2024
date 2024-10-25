
## splitext--------------------> splits the extension from a path name.Extension is everything from last dot.


import os
files = os.listdir()

for file in files:
    print(os.path.splitext(file))

# Splitdrive

import os

path = "/home/file.txt"
drive, tail = os.path.splitdrive(path)

print("Drive:", drive)  
print("Tail:", tail)    