#!/usr/bin/python3


DOZEN = 12
DISCOUNT = 2
GST = 12.5

# cost of fruits
cost_of_apple = 12 # per piece
cost_of_mango = 34 # per piece
# Quantities of fruits
qty_of_apples = 5 * DOZEN
qty_of_mangos = 3 * DOZEN
# pieces
# pieces
# Selling Price Computation
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos # PEDMAS
# total_sp =(cost_of apple + qty of apples) + (cost of mango* qty_of_mangos) # PEDMAS
print("total selling price ",total_sp)
discount_amount = (total_sp * DISCOUNT) / 100
print ("Discount Amount  ", discount_amount)
# Payable Amount Calculation
payable_amount = (total_sp - discount_amount)
print("Payable Amount :",  payable_amount)
# GST Calculation
gst_on_fruits = (payable_amount * GST) / 100
print("GST on Fruits  :", gst_on_fruits)
# Billable amount
billable_amount = payable_amount+ gst_on_fruits
print("billable amount", billable_amount)

#round function
print("billable amount(r) :", round(billable_amount, 2))