#!/usr/bin/python
import json
from pprint import pprint

book = {}
book["title"] = "Python Programming Essentials"
book["tags"] = ("Python", "Programming")
book["published"] = True
book["comment_link"] = None
book["author"] = "Udhay"
book["id"] = 786

print("\nbook details :\n", book)
print("type(book) is ", type(book))
pprint(book)

# Serilazation
with open("ebook.json", "w") as f:
    json.dump(book, f)
    f.close()

# De-serialization
print("\ndeserializing the json data \n")
with open("ebook.json", "r") as g:
    data = json.load(g)
    g.close()

print("data = ", data)

print("\nprinting using pretty print")
pprint(data)
pprint(data, indent=4)


print("convert dictionary to JSON string:")  
json_string = json.dumps(book, indent=4)  
print(json_string)

print("convert JSON string back to dictionary:")  
json_dict = json.loads(json_string)  
print("Dict data:", json_dict)
pprint(json_dict, indent=4)