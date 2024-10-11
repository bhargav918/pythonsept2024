


# Assignment -- apply all loigical and relationsl operat8ons on the sets; and understand the results

#LOGICAL Operations   #Union (| or union()):
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b  # or set_a.union(set_b)
print(union_set)

#Intersection (& or intersection()):
intersection_set = set_a & set_b  # or set_a.intersection(set_b)
print(intersection_set) 

#difference
difference_set = set_a - set_b  # or set_a.difference(set_b)
print(difference_set)

#Symmetric Difference (^ or symmetric_difference()):
symmetric_difference_set = set_a ^ set_b  
print(symmetric_difference_set)

################# RELATIONAL OPS#####################


#Subset (<= or issubset()):
set_c = {1, 2}
is_subset = set_c <= set_a  # or set_c.issubset(set_a)
print(is_subset) 

#Superset (>= or issuperset()):
is_superset = set_a >= set_c  # or set_a.issuperset(set_c)
print(is_superset)

#Disjoint (isdisjoint()):
set_d = {6, 7}
are_disjoint = set_a.isdisjoint(set_d)
print(are_disjoint)










#Method 2
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# set_c = {1, 2}
# set_d = {6, 7}

# # Logical operations
# print("Union:", set_a | set_b)
# print("Intersection:", set_a & set_b)
# print("Difference:", set_a - set_b)
# print("Symmetric Difference:", set_a ^ set_b)

# # Relational operations
# print("Is set_c a subset of set_a?", set_c <= set_a)
# print("Is set_a a superset of set_c?", set_a >= set_c)
# print("Are set_a and set_d disjoint?", set_a.isdisjoint(set_d))