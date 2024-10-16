
# Defining strings in different languages
strings = {
    "English": "Hello",
    "Spanish": "Hola",
    "French": "Bonjour",

}

# Iterate over strings
for language, text in strings.items():            #here items() returns key value pairs(language and text)
    print(f"{language}: {text}")
    print(f"UTF-8 encoded: {text.encode('utf-8')}") # it converts strings to byecode




















        #here items() returns key value pairs(language and text)