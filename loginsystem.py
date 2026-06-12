# a login system using username and password

correct_user = "admin"
correct_pass = "password123"

username = input("Username: ")
password = input("Password: ")

if username == correct_user and password == correct_pass:
    print("Login successful.")
else:
    print("Invalid credentials.")