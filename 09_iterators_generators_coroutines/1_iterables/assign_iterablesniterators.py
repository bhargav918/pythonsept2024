# Assignment - try all iterables and create iterators  :
import itertools
iterables = {
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"a": 7, "b": 8},
    "set": {9, 10, 11},
    "string": "bhargav",
}

iterators = {
    "list": iter(iterables["list"]),
    "tuple": iter(iterables["tuple"]),
    "dict": iter(iterables["dict"].items()),
    "set": iter(iterables["set"]),
    "string": iter(iterables["string"]),
}

for type, iterator in iterators.items():
    print(f"{type} iteration:")
    for item in iterator:
        print(item)