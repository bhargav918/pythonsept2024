#!/usr/bin/python3

"""
Algorithm
-------------------
grocery store py P
Step 1: Get the cost of itens
into variables
Step 2: Get the quantity of items from the user(in run time)

"""

# cost of items
cost_of_rice = 10   # per kg
cost_of_wheat = 34 

qty_of_rice = int(input("Enter Qty. of rice(in Kgs) :"))
print("qty of rice :", qty_of_rice, type(qty_of_rice))

qty_of_wheat = int(input("Enter Qty. of wheat(in Kgs) :"))
print("Qty of Wheat :", qty_of_wheat, type(qty_of_wheat))

# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of Rice :", sp_of_rice)
sp_of_wheat = cost_of_wheat * qty_of_wheat
print ("SP of wheat :", sp_of_wheat)