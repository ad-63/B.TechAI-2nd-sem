# to input roll no, name, age of a student and display them using diff output formatting.

roll = input("Enter roll no: ")
name = input("Enter name: ")
age = input("Enter age: ")

print(f"Name: {name}, Roll: {roll}, Age: {age}")
print("Name: {}, Roll: {}, Age: {}".format(name, roll, age))