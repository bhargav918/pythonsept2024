#/usr/bin/python3

"""
Purpose: Saving Bank
    
    Initial Balance 0

Algorithm
---------------------------
Step 1: Create an variable balance: with initial value o
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
step 6: Display balance
"""
 
balance = 0
print("Account opening balance is", balance)  #Create an variable balance: with initial value o
balance = balance + 1500
print("Account Balance after minimum deposit is", balance) #Initial Despoit of min balance 1500
balance = balance + 3300
print("Account Balance after salary credit is", balance) #Salary credited of 3300
balance = balance - 33.33
print("Account Balance after online purchase is", balance) #online purchase of 33.33
balance = balance - 1500
print("Account Balance after deducting rent is", balance) #House Rent paid of 1500

display_balance = balance   # (0 + 1500 + 3300 - 33.33 - 1500) = 3266.67
print("Remaining balance is ", round(balance , 2))  # display balance

