# to determine ticket catagory based on age

age = int(input("Enter age: "))
if age < 13:
    print("Category: Child")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")