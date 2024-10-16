import itertools

# Iterable types
iterables = {
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"a": 7, "b": 8},
    "set": {9, 10, 11},
    "string": "hello",
}

# Creating iterators
iterators = {
    "list": iter(iterables["list"]),
    "tuple": iter(iterables["tuple"]),
    "dict": iter(iterables["dict"].items()),
    "set": iter(iterables["set"]),
    "string": iter(iterables["string"]),
}
# Iterate over iterables
for type, iterator in iterators.items():
    print(f"{type.capitalize()} iteration:")
    for item in iterator:
        print(item)









        












        # Creates iterators for each iterable type using the iter() function.
        # items() is used for dictionaries to iterate over key-value pairs.
    