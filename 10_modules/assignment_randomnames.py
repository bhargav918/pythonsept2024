import random

first_names = { "male" : ("rehman", "pratik"),"female": ("fabina", "teju")}
last_names = ("Bush", "Mohammed", "woods", "modi")

# for i in range(10):
#     rdm_first_name = random.choice(first_names)
#     rdm_last_name = random.choice(last_names)
#     print(f"{rdm_first_name} {rdm_last_name}")
def generate_names(_first_names, _last_names, count):
    _names = list()
    for i in range(count):
        rdm_first_name = random.choice(_first_names[gender])
        rdm_last_name = random.choice(_last_names)
        _names.append(f"{rdm_first_name} {rdm_last_name}")
    return _names
    
gender = input("Enter gender male or female: ").strip().lower()

if gender in first_names.keys():
    names = generate_names(first_names,last_names, 10)
    print("Generated Names:")
    for name in names:
        print(name)