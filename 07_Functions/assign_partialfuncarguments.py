#Partial functions in Python is a function that is created by fixing a certain number of arguments of another function. 
## assignment -- implement partial function with all types of args -- defaults args functions, vaaridica functions

from functools import partial
def add(a, b):                            # Simple Function
    return a + b

# Partial Function with Default Argument
default_arg = partial(add, b=5)
print(default_arg(10))                    # o/p : 15
#---------------------------------------------------------------
# Partial Function with Variable Arguments (*args)
def sum_numbers(*args):
    return sum(args)

variable_args = partial(sum_numbers, 1, 2, 3)
print(variable_args())  # O/p: 6
print(variable_args(4, 5))  # O/p: 15
#------------------------------------------
# Partial Function with Variable Keyword Arguments (**kwargs)
def greets(name, msg="Birthday"):
    return f"Hi, {name}! Happy {msg}!!!"

greetings = partial(greets, name="Bhargav")
print(greetings())
#------------------------------------------
# Partial Function with Mixed Arguments
def calculate(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}, args: {args}, kwargs: {kwargs}")
    return a + b + sum(args)

calculate_with_defaults = partial(calculate, 10, 20)          # calling the partial func
result = calculate_with_defaults(30, 40, c=50)                #calling function with additional args
print("Result:", result)



