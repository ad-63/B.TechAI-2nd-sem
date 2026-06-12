# to find cube of a number.
# def cube(n):
#     return n ** 3

# num = float(input("Enter a number: "))
# print(f"The cube is: {cube(num)}")

# to check palimdrum
# def is_palindrome(n):
#     s = str(n)
#     return s == s[::-1]

# num = input("Enter a number: ")
# if is_palindrome(num):
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")

# to count vowel strings
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in text if char in vowels)

# s = input("Enter a string: ")
# print(f"Number of vowels: {count_vowels(s)}")

# to find smellest and largest element in a list
# def find_min_max(numbers):
#     return min(numbers), max(numbers)

# nums = [float(x) for x in input("Enter numbers separated by space: ").split()]
# minimum, maximum = find_min_max(nums)
# print(f"Smallest: {minimum}, Largest: {maximum}")

# to display customer with highest balance.
# customers = []
# for i in range(3):
#     name = input(f"Customer {i+1} name: ")
#     balance = float(input("Balance: "))
#     customers.append({"name": name, "balance": balance})

# highest = max(customers, key=lambda x: x['balance'])
# print(f"Customer with highest balance: {highest['name']} (${highest['balance']})")

# to display the employee with highest salary
# employees = []
# for i in range(10):
#     name = input(f"Employee {i+1} name: ")
#     salary = float(input("Salary: "))
#     employees.append({"name": name, "salary": salary})

# highest = max(employees, key=lambda x: x['salary'])
# print(f"Highest salary: {highest['name']} (${highest['salary']})")

# most expensive product
# n = int(input("Enter number of products: "))
# products = []
# for i in range(n):
#     name = input("Product name: ")
#     price = float(input("Price: "))
#     products.append({"name": name, "price": price})

# expensive = max(products, key=lambda x: x['price'])
# print(f"Most expensive: {expensive['name']} (${expensive['price']})")

# student above 18
# n = int(input("Enter number of students: "))
# count = 0
# for i in range(n):
#     age = int(input(f"Enter age of student {i+1}: "))
#     if age > 18:
#         count += 1
# print(f"Students above 18 years old: {count}")

#displaying the oldest patient.
# class HospitalPatient:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# n = int(input("Enter number of patients: "))
# patients = []
# for i in range(n):
#     name = input("Name: ")
#     age = int(input("Age: "))
#     patients.append(HospitalPatient(name, age))

# oldest = max(patients, key=lambda p: p.age)
# print(f"The oldest patient is {oldest.name}, aged {oldest.age}.")