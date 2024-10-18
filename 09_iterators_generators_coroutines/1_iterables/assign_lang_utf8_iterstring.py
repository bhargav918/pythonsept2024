# assignment - try with utf-8 differebt lanugages for iter string
strings = {
    "English": "Hello",
    "Spanish": "Hola",
    "French": "Bonjour",

}
string_iter = iter(strings.items())
print(f"{type(string_iter)},{string_iter}")

for language, text in string_iter:            
    print(f"{language}: {text}")