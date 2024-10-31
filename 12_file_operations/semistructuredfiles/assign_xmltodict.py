#!/usr/bin/python
""" Purpose: XML to python DICT conversion and vice versa """

from pprint import pprint
import xmltodict 


try:
    import xmltodict 
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system
    system("pip install xmltodict --user")
    import xmltodict 


with open("books.xml", "r") as fh:
    file_content = fh.read()
doc = xmltodict.parse(file_content)

pprint(doc)

mapping = {}
for each in doc["catalog"]["book"]:
    mapping[each["@isbn"]] = each["title"]

pprint(mapping)

xml_data = {
    "catalog": {
        "book": [{"@isbn": isbn, "title": title} for isbn, title in mapping.items()]
    }
}


xml_output = xmltodict.unparse(xml_data, pretty=True)

print("\nConverted back to XML:")
print(xml_output)

with open("converted_books.xml", "w") as xml_file:
    xml_file.write(xml_output)