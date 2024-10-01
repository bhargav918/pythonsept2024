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
print("simple interest is :" , total_amount)


#compound interest

principal_amount_p = float(input("Enter the principal amount:"))

interest_rate = float(input("Enter the interest rate r:")) / 100
print("Interest rate is :" , interest_rate)

no_of_periods_n = int(input("Enter the no. of periods:"))

time_t = float(input("Enter the time in years"))

# Formula for CI= P*(1 + R/n)**(n*t)

CI = principal_amount_p * (1 + interest_rate / no_of_periods_n)**(no_of_periods_n * time_t)
print("compound interest is", round(CI, 2))









