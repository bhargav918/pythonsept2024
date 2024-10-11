

#The commutative property of multiplication states that the sequence wherein two integers are multiplied does not affect the complete outcome. The graphic below depicts the commutative property of 2 different multiplications.
  #a*b =b*a

A = [1, 2, 3]
B = [4, 5, 6]

# Define repetition counts
n = 2
m = 3

# Repeating lists
result1 = A * n + B * m
result2 = B * m + A * n

# Output the results
print("A repeated n times and B repeated m times:", result1)
print("B repeated m times and A repeated n times:", result2)

# Check if they are equal
commutative = (result1 == result2)
print("check this is commutative or not :", commutative)
