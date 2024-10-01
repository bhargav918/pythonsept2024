#/usr/bin/python3

# simple interest A=P(1+rt)
# https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

principal_amount = float(input("Enter the priciple balance $:"))
print("Principle balance is $", principal_amount)

interest_rate = float(input("Enter the interest rate r:")) / 100
print("Interest rate is :" , interest_rate)

time = int(input("Enter Time in years t:"))
print("Time in years :", time)

total_amount = principal_amount * (1 + interest_rate * time)
print("Total amount is :" , total_amount)











