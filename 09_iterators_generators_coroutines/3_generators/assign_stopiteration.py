# how to get the return message as stopIteration excetion message in python

def stop_iteration():
    yield 123
    yield 456
    return "bhargav"

generator = stop_iteration()

try:
    while True:
        print(next(generator))
except StopIteration as ex:
    print(ex)