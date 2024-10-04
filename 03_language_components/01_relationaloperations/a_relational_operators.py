#!/usr/bin/python3
"""
Purpose: Relational Operations
    - These operations will result in a boolean value (True or False)
    ‹ lesser
    > greater == equal to
    <= less than or equal to
    ›= greater than or equal to
    != not equal to
    <> not equal to ( in python 2 only)
    """

us_dollar = 86
candian_dollar = 50
print("us_dollar :",us_dollar)
print("candian_dollar :",candian_dollar)

print(f"us_dollar = {us_dollar}")
print(f"candian_dollar = {candian_dollar}")

print(f"{us_dollar    =}")
print(f"{candian_dollar    =}")
print()

print(f"us_dollar == candian_dollar",us_dollar == candian_dollar)
print(f"{us_dollar == candian_dollar = }")

print(f"us_dollar  =  {us_dollar}")
print(f"candian_dollar  =  {candian_dollar}")

print(f"{us_dollar > candian_dollar =}")
print(f"{us_dollar >= candian_dollar =}")
print(f"{us_dollar < candian_dollar =}")
print(f"{us_dollar <= candian_dollar =}")
print(f"{us_dollar > candian_dollar =}")
print(f"{us_dollar != candian_dollar =}")
#print(f"{us_dollar <> candian_dollar =}")  #works only in python 2.0


print(f"{74 == 50 =}")
print(f"{74 != 50 =}")
print(f"{74 >= 50 =}")
print(f"{74 <= 50 =}")


str1="abc"
str2="abc"
print(f"{str1 == str2 =}")
print(f"{str1 != str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 >= str2 =}")

str1="abc"
str2="bc"
print(f"{str1 == str2 =}")
print(f"{str1 != str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 >= str2 =}")