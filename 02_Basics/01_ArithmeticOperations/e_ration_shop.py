#!/usr/bin/python3

"""
Algorithm
-----------------------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items into variables
Step 3: Compute the selling price to each item and and them.
step 4: calculate the subsidy amount and substract from the selling price
"""

cost_of_wheat = 25  #per kg
cost_of_rice = 12

quantity_of_wheat = 30
quantity_of_rice = 50

sp_of_wheat = cost_of_wheat * quantity_of_wheat
sp_of_rice = cost_of_rice * quantity_of_rice

total_sp = sp_of_wheat + sp_of_rice
print("Total selling price is ", total_sp)
subsidy_amount = total_sp * (20/100)
print("subsidy_amount: ", subsidy_amount)

Billable_amount = total_sp - subsidy_amount
print("Billable amount", Billable_amount)