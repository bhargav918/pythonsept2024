#!/usr/bin/python3


"""
purpose: Demonstraion of usage of help() on python objects
"""

dozen = 12
dozen = 12.4
dozen = None
dozen = True
print(f"{type(dozen) =}")
print(f"{id(dozen) =}")
print(f"{dozen      =}")
print(f"{dir(dozen) =}")

help(dozen)       # to exit enter q

#python -m pydoc int
#python -m pydoc -k int
