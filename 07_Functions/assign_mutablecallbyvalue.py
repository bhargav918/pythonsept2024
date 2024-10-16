# ----------- Call by value for immutable objects-------------------------

# By Default, 
#     for mutable object, It is call by reference == changes in function will reflect output
#                         call by value  with did .copy()
#     for immutable object, It is call by value == changes in function will NOT reflect output
#                         call by reference  with global declaration

# call by value ---> changes in function will NOT reflect output
# call by refrence ---> changes in function will reflect output

def change_int(n):                            # int
    n = 10
    print("Inside function:", n)
num = 5
change_int(num)
print("Outside function:", num)
#-----------------------------------------
def change_float(n):                           #float
    n = 10.5
    print("Inside function:", n)
num = 5.2
change_float(num)
print("Outside function:", num)

#------------------------------------------------
def change_none(n):                           # None
    n = "none"
    print("Inside function:", n)
var = None
change_none(var)
print("Outside function:", var)

#-------------------------
def change_bool(b):                     # boolean
    b = True
    print("Inside function:", b)

flag = False
change_bool(flag)
print("Outside function:", flag)
#------------------------------------------
def change_str(s):                    # string
    s = "New String"
    print("Inside function:", s)

text = "Original String"
change_str(text)
print("Outside function:", text)
#-------------------------------
def change_frozenset(fs):
    fs = frozenset({1, 2, 3})          # frozenset
    print("Inside function:", fs)

fs = frozenset({4, 5, 6})
change_frozenset(fs)
print("Outside function:", fs)