from itertools import islice

strings = "slicing index"
lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuples = (10, 20, 30, 40, 50, 60)
dicts = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6}

def slicing_with_islice(iterable, name):
    print(f"{name} Original: {iterable}")
    slicing_index = list(islice(iterable, 5))      # Slicing 1st 5 elements
    print(f"{name} Sliced (first 5 elements): {slicing_index}")
    print()

slicing_with_islice(strings, "String")
slicing_with_islice(lists, "List")
slicing_with_islice(tuples, "Tuple")
slicing_with_islice(dicts.keys(), "Dictionary Keys")
slicing_with_islice(dicts.values(), "Dictionary Values")

