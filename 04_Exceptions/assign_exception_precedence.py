try:
    
    num1 = 100
    num2 = 200
    num3 = int("123")  
    user_input = input("Enter a mathematical expression: ")
    expr = eval(user_input)

except Exception as e:
    print(f"{e=}")
else:
    print("No exception - So, in else block")
    print(f"The result of the expression is: {expr}")