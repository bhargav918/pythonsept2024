
##List:  Call by reference  \
# By Default, 
#     for mutable object, It is call by reference == changes in function will reflect output
#                         call by value  with did .copy()
#     for immutable object, It is call by value == changes in function will NOT reflect output
#                         call by reference  with global declaration

# call by value ---> changes in function will NOT reflect output
# call by refrence ---> changes in function will reflect output


def change_list(lists):
    lists.append(10)
    print("Inside function:", lists)

numbers = [1, 2, 3]
change_list(numbers)
print("Outside function:", numbers)
#--------------------------SETS-------------------
def change_set(s):
    s.add(10)
    print("Inside function:", s)

numbers = {1, 2, 3}
change_set(numbers)
print("Outside function:", numbers)
#-------------------------Dict----------------------
def change_dict(d):
    d.update({'new_key': 'new_value'})
    print("Inside function:", d)

data = {'key': 'value'}
change_dict(data)
print("Outside function:", data)


