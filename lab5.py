# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     result = a / b
#     print(f"Result: {result}")

#     lst = [10, 20, 30]
#     index = int(input("Enter index to access (0-2): "))
#     print(f"Value at index: {lst[index]}")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input, please enter a number.")
# except IndexError:
#     print("Error: Index out of range.")


# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     print("Error: Please enter a valid number.")
# finally:
#     print("Execution completed. This block always runs.")




# class InsufficientBalanceError(Exception):
#     pass


# class InvalidAmountError(Exception):
#     pass


# def withdraw(balance, amount):
#     if amount <= 0:
#         raise InvalidAmountError("Withdrawal amount must be positive.")
#     if amount > balance:
#         raise InsufficientBalanceError("Insufficient balance for this withdrawal.")
#     return balance - amount


# balance = 5000
# try:
#     amount = float(input("Enter amount to withdraw: "))
#     balance = withdraw(balance, amount)
#     print(f"Withdrawal successful. New Balance: {balance}")
# except InsufficientBalanceError as e:
#     print(f"Error: {e}")
# # except InvalidAmountError as e:
#     print(f"Error: {e}")



# class InvalidAccountNumberError(Exception):
#     pass


# class InvalidPINError(Exception):
#     pass


# class InvalidTransactionAmountError(Exception):
#     pass


# def validate_transaction(account_number, pin, amount):
#     if len(str(account_number)) != 10:
#         raise InvalidAccountNumberError("Account number must be 10 digits.")
#     if len(str(pin)) != 4:
#         raise InvalidPINError("PIN must be 4 digits.")
#     if amount <= 0:
#         raise InvalidTransactionAmountError("Transaction amount must be positive.")
#     print("Transaction validated successfully.")


# try:
#     account_number = input("Enter account number: ")
#     pin = input("Enter PIN: ")
#     amount = float(input("Enter transaction amount: "))
#     validate_transaction(account_number, pin, amount)
# except InvalidAccountNumberError as e:
#     print(f"Error: {e}")
# except InvalidPINError as e:
#     print(f"Error: {e}")
# except InvalidTransactionAmountError as e:
#     print(f"Error: {e}")




# n = int(input("Enter number of students: "))
# with open("student_details.txt", "w") as f:
#     for i in range(n):
#         name = input("Enter name: ")
#         address = input("Enter address: ")
#         age = input("Enter age: ")
#         f.write(f"{name},{address},{age}\n")

# print("\nStudents from Kathmandu:")
# with open("student_details.txt", "r") as f:
#     for line in f:
#         name, address, age = line.strip().split(",")
#         if address.lower() == "kathmandu":
#             print(f"Name: {name}, Address: {address}, Age: {age}")





# n = int(input("Enter number of employees: "))
# with open("employee_details.txt", "w") as f:
#     for i in range(n):
#         name = input("Enter name: ")
#         emp_id = input("Enter employee ID: ")
#         salary = float(input("Enter salary: "))
#         f.write(f"{name},{emp_id},{salary}\n")

# updated_records = []
# with open("employee_details.txt", "r") as f:
#     for line in f:
#         name, emp_id, salary = line.strip().split(",")
#         salary = float(salary) * 1.10
#         updated_records.append(f"{name},{emp_id},{salary}\n")

# with open("employee_details.txt", "w") as f:
#     f.writelines(updated_records)

# print("\nUpdated Employee Records:")
# with open("employee_details.txt", "r") as f:
#     for line in f:
#         name, emp_id, salary = line.strip().split(",")
#         print(f"Name: {name}, Employee ID: {emp_id}, Updated Salary: {salary}")




# n = int(input("Enter number of students: "))
# with open("student_marks.txt", "w") as f:
#     for i in range(n):
#         roll = input("Enter roll number: ")
#         name = input("Enter name: ")
#         marks = input("Enter marks: ")
#         f.write(f"{roll},{name},{marks}\n")

# print("\nStudents with marks above 80:")
# with open("student_marks.txt", "r") as f:
#     for line in f:
#         roll, name, marks = line.strip().split(",")
#         if float(marks) > 80:
#             print(f"Roll Number: {roll}, Name: {name}, Marks: {marks}")2




# n = int(input("Enter number of students: "))
# with open("students.txt", "w") as f:
#     for i in range(n):
#         roll = input("Enter roll number: ")
#         name = input("Enter name: ")
#         marks = input("Enter marks: ")
#         f.write(f"{roll},{name},{marks}\n")

# search_roll = input("\nEnter roll number to search: ")
# found = False
# with open("students.txt", "r") as f:
#     for line in f:
#         roll, name, marks = line.strip().split(",")
#         if roll == search_roll:
#             print(f"Roll Number: {roll}, Name: {name}, Marks: {marks}")
#             found = True
#             break

# if not found:
#     print("Student with this roll number not found.")2





# filename = input("Enter the filename to read: ")
# try:
#     with open(filename, "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: The file was not found.")
# except PermissionError:
#     print("Error: You do not have permission to access this file.")
# except FileExistsError:
#     print("Error: The file already exists.")even




# source_file = input("Enter the source filename: ")
# destination_file = input("Enter the destination filename: ")

# try:
#     with open(source_file, "r") as src, open(destination_file, "w") as dest:
#         content = src.read()
#         dest.write(content)
#     print("File copied successfully!")
# except FileNotFoundError:
#     print("Error: Source file not found.")
# except PermissionError:
#     print("Error: Permission denied.")

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)
print("Server waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")
conn.send("Welcome to Orchid College".encode())
conn.close()
server.close()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
message = client.recv(1024).decode()
print(f"Message from server: {message}")
client.close()


