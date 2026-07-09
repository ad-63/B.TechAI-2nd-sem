# # n = int(input("Enter number of students: "))
# # with open("student_details.txt", "w") as f:
# #     for i in range(n):
# #         name = input("Enter name: ")
# #         address = input("Enter address: ")
# #         age = input("Enter age: ")
# #         f.write(f"{name},{address},{age}\n")

# # print("\nStudents from Kathmandu:")
# # with open("student_details.txt", "r") as f:
# #     for line in f:
# # #         name, address, age = line.strip().split(",")
# # #         if address.lower() == "kathmandu":
# # #             print(f"Name: {name}, Address: {address}, Age: {age}")


# # n = int(input("Enter number of employees: "))
# # with open("employee_details.txt", "w") as f:
# #     for i in range(n):
# #         name = input("Enter name: ")
# #         emp_id = input("Enter employee ID: ")
# #         salary = float(input("Enter salary: "))
# #         f.write(f"{name},{emp_id},{salary}\n")

# # updated_records = []
# # with open("employee_details.txt", "r") as f:
# #     for line in f:
# #         name, emp_id, salary = line.strip().split(",")
# #         salary = float(salary) * 1.10
# #         updated_records.append(f"{name},{emp_id},{salary}\n")

# # with open("employee_details.txt", "w") as f:
# #     f.writelines(updated_records)

# # print("\nUpdated Employee Records:")
# # with open("employee_details.txt", "r") as f:
# #     for line in f:
# #         name, emp_id, salary = line.strip().split(",")
# #         print(f"Name: {name}, Employee ID: {emp_id}, Updated Salary: {salary}")2


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
#     print("Error: The file already exists.")


source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

try:
    with open(source_file, "r") as src, open(destination_file, "w") as dest:
        content = src.read()
        dest.write(content)
    print("File copied successfully!")
except FileNotFoundError:
    print("Error: Source file not found.")
except PermissionError:
    print("Error: Permission denied.")