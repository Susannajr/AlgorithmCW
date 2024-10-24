keys = ["name", "surname", "age"]
value = input("Please enter name, surname and age separated with a space ").split(" ")
#Example of input 'Susanna Smbatyan 19

custom_dict = dict(zip(keys, value))

print("Your custom dictionary is: ", custom_dict)
