# assignmnet - -try isclice on all itersable objects which supoport indexing and sclicing

from itertools import islice

strings = "slicing index"
lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tuples = (10, 20, 30, 40, 50, 60)
dicts = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6}

def slicing_islice(iterable, name):
    slicing_index = list(islice(iterable, 5))     
    print(f"{name} Sliced (first 5 elements): {slicing_index}")
    print()

slicing_islice(strings, "String")
slicing_islice(lists, "List")
slicing_islice(tuples, "Tuple")
slicing_islice(dicts.items(), "Dictionary Keys")