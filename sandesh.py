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