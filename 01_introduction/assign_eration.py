#!/usr/bin/python3

rice_price = 12 
rice_quantity = 25
subsidy = 65
rice_cost = rice_price * rice_quantity  
rice_cost = (12 * 25)
print(rice_cost)

wheat_price = 25
wheat_quantity = 20
wheat_cost = wheat_price * wheat_quantity
wheat_cost = (25 * 20)
print(wheat_cost)

total_cost = rice_cost + wheat_cost
print("total_cost", total_cost)
final_cost = total_cost - subsidy
print("Final cost after subsidy", final_cost)