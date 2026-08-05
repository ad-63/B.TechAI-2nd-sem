# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="adwitiya123"
#     )
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS OfficeDB")
#     print("Database 'OfficeDB' created successfully.")

#     conn.database = "OfficeDB"
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS Employee (
#             emp_id INT PRIMARY KEY,
#             emp_name VARCHAR(100),
#             age INT,
#             gender VARCHAR(10),
#             department VARCHAR(50),
#             salary DECIMAL(10,2)
#         )
#     """ 
#     cursor.execute(create_table_query)
#     print("Table 'Employee' created successfully.")

#     cursor.close()
#     conn.close()

# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL: {e}")


# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="adwitiya123",
#         database="OfficeDB"
#     )
#     cursor = conn.cursor()

#     n = int(input("Enter number of employees: "))
#     for i in range(n):
#         emp_id = int(input("Enter Employee ID: "))
#         emp_name = input("Enter Employee Name: ")
#         age = int(input("Enter Age: "))
#         gender = input("Enter Gender: ")
#         department = input("Enter Department: ")
#         salary = float(input("Enter Salary: "))

#         insert_query = """
#             INSERT INTO Employee (emp_id, emp_name, age, gender, department, salary)
#             VALUES (%s, %s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_query, (emp_id, emp_name, age, gender, department, salary))

#     conn.commit()
#     print("Employee records inserted successfully.")

#     cursor.execute("SELECT * FROM Employee")
#     rows = cursor.fetchall()
#     print("\nAll Employee Records:")
#     for row in rows:
#         print(row)

#     cursor.close()
#     conn.close()

# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL: {e}")





# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="adwitiya123",
#         database="OfficeDB"
#     )
#     cursor = conn.cursor()

#     emp_id = int(input("Enter Employee ID to search: "))
#     cursor.execute("SELECT * FROM Employee WHERE emp_id = %s", (emp_id,))
#     result = cursor.fetchone()

#     if result:
#         print(f"Employee Found: {result}")
#     else:
#         print("Employee not found.")

#     cursor.close()
#     conn.close()

# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL: {e}")





# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="adwitiya123",
#         database="OfficeDB"
#     )
#     cursor = conn.cursor()

#     emp_id = int(input("Enter Employee ID to update: "))
#     new_salary = float(input("Enter new salary: "))
#     new_department = input("Enter new department: ")

#     update_query = """
#         UPDATE Employee
#         SET salary = %s, department = %s
#         WHERE emp_id = %s
#     """
#     cursor.execute(update_query, (new_salary, new_department, emp_id))
#     conn.commit()
#     print("Employee record updated successfully.")

#     cursor.execute("SELECT * FROM Employee WHERE emp_id = %s", (emp_id,))
#     result = cursor.fetchone()
#     print(f"Updated Record: {result}")

#     cursor.close()
#     conn.close()

# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL: {e}")



# import mysql.connector
# from mysql.connector import ProgrammingError, IntegrityError, OperationalError

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="adwitiya123",
#         database="OfficeDB"
#     )
#     cursor = conn.cursor()

#     insert_query = """
#         INSERT INTO Employee (emp_id, emp_name, age, gender, department, salary)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     cursor.execute(insert_query, (1, "Test User", 25, "Male", "IT", 30000))
#     conn.commit()
#     print("Employee inserted successfully.")

#     cursor.close()
#     conn.close()

# except ProgrammingError as e:
#     print(f"Programming Error: {e}")
# except IntegrityError as e:
#     print(f"Integrity Error: {e}")
# except OperationalError as e:
#     print(f"Operational Error: {e}")
# except mysql.connector.Error as e:
#     print(f"Database Error: {e}")



# # 

# # 
# # 



# 

# import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="adwitiya123",
#         database="OfficeDB"
#     )
#     cursor = conn.cursor()

#     def create_employee():
#         emp_id = int(input("Enter Employee ID: "))
#         emp_name = input("Enter Employee Name: ")
#         age = int(input("Enter Age: "))
#         gender = input("Enter Gender: ")
#         department = input("Enter Department: ")
#         salary = float(input("Enter Salary: "))
#         try:
#             insert_query = """
#                 INSERT INTO Employee (emp_id, emp_name, age, gender, department, salary)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             """
#             cursor.execute(insert_query, (emp_id, emp_name, age, gender, department, salary))
#             conn.commit()
#             print("Employee added successfully.")
#         except mysql.connector.Error as e:
#             print(f"Error: {e}")

#     def read_employees():
#         cursor.execute("SELECT * FROM Employee")
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)

#     def update_employee():
#         emp_id = int(input("Enter Employee ID to update: "))
#         new_salary = float(input("Enter new salary: "))
#         try:
#             cursor.execute("UPDATE Employee SET salary = %s WHERE emp_id = %s", (new_salary, emp_id))
#             conn.commit()
#             print("Employee updated successfully.")
#         except mysql.connector.Error as e:
#             print(f"Error: {e}")

#     def delete_employee():
#         emp_id = int(input("Enter Employee ID to delete: "))
#         try:
#             cursor.execute("DELETE FROM Employee WHERE emp_id = %s", (emp_id,))
#             conn.commit()
#             print("Employee deleted successfully.")
#         except mysql.connector.Error as e:
#             print(f"Error: {e}")

#     while True:
#         print("\n1. Create  2. Read  3. Update  4. Delete  5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             create_employee()
#         elif choice == "2":
#             read_employees()
#         elif choice == "3":
#             update_employee()
#         elif choice == "4":
#             delete_employee()
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice.")

#     cursor.close()
#     conn.close()

# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL: {e}")

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS officeDB")
cur.execute("USE officeDB")

cur.execute("""
CREATE TABLE IF NOT EXISTS Employee(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    department VARCHAR(30),
    salary FLOAT
)
""")

print("Database and Table Created Successfully")

con.close()






import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="officeDB"
)

cur = con.cursor()

n = int(input("Enter Number of Employees: "))

for i in range(n):
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    dept = input("Department: ")
    salary = float(input("Salary: "))

    sql = "INSERT INTO Employee VALUES(%s,%s,%s,%s,%s,%s)"
    val = (emp_id,name,age,