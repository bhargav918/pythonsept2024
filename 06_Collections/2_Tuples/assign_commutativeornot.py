 # 1. Prove that tuple concatenation is not commutative: t1 + t2 != t2 + t1

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# # Concatenate t1 and t2
t1_result1 = t1 + t2
print("t1 + t2:", t1_result1)

# Concatenate t2 and t1
t2_result2 = t2 + t1
print("t2 + t1:", t2_result2)

tuple = (t1_result1 == t2_result2)
print("Check both tuples are equal or not =", tuple)

#Prove that tuple repetition is commutative       : t1 * 3 == 3 * t1

t1 = (1, 2, 3)

t1_result1 = t1 * 3
print("t1 * 3:", t1_result1)
t2_result2 = 3 * t1
print("3 * t1:", t2_result2)

# Check if they are equal
tuple = (t1_result1 == t2_result2)
print("Check both tuples are equal or not =", tuple)