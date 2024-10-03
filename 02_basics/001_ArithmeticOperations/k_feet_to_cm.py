#/usr/bin/python3

"""
feet to centimeter converstion
    1 foot - 12 inches
    1 inch - 2.54 centimeter
"""

height_feet=int(input("Enter the height in feet:"))    
height_inch = height_feet * 12
height_cms = height_inch * 2.54
print("height in inches :" , height_inch)
print("height in cms", height_cms)
     
