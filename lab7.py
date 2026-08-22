# import tkinter as tk

# def submit():
#     result.config(text=f"Name: {name.get()}\nAge: {age.get()}\nGender: {gender.get()}\nAddress: {address.get()}\nLanguages: {lang.get()}")

# root = tk.Tk()
# root.title("Student Information Form")

# tk.Label(root, text="Name").grid(row=0, column=0)
# name = tk.Entry(root)
# name.grid(row=0, column=1)

# tk.Label(root, text="Age").grid(row=1, column=0)
# age = tk.Entry(root)
# age.grid(row=1, column=1)

# tk.Label(root, text="Gender").grid(row=2, column=0)
# gender = tk.Entry(root)
# gender.grid(row=2, column=1)

# tk.Label(root, text="Address").grid(row=3, column=0)
# address = tk.Entry(root)
# address.grid(row=3, column=1)

# tk.Label(root, text="Favorite Languages").grid(row=4, column=0)
# lang = tk.Entry(root)
# lang.grid(row=4, column=1)

# tk.Button(root, text="Submit", command=submit).grid(row=5, column=0, columnspan=2)
# result = tk.Label(root, text="")
# result.grid(row=6, column=0, columnspan=2)

# root.mainloop()

#............................................................


# import tkinter as tk

# root = tk.Tk()
# root.title("Notes Taking Application")

# entry = tk.Entry(root, width=40)
# entry.pack()

# frame = tk.Frame(root)
# frame.pack()

# def add_note():
#     text = entry.get()
#     if text:
#         row = tk.Frame(frame)
#         row.pack(fill="x")
#         label = tk.Label(row, text=text)
#         label.pack(side="left")
#         tk.Button(row, text="Edit", command=lambda: edit_note(label)).pack(side="right")
#         tk.Button(row, text="Delete", command=row.destroy).pack(side="right")
#         entry.delete(0, tk.END)

# def edit_note(label):
#     new_text = entry.get()
#     if new_text:
#         label.config(text=new_text)
#         entry.delete(0, tk.END)

# tk.Button(root, text="Add Note", command=add_note).pack()

# root.mainloop()


#............................................................



# import tkinter as tk
# import mysql.connector

# conn = mysql.connector.connect(host="localhost", user="root", password="adwitiya123")
# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS officeDB")
# conn.database = "officeDB"
# cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50), password VARCHAR(50))")
# cursor.execute("SELECT COUNT(*) FROM users")
# if cursor.fetchone()[0] == 0:
#     cursor.executemany("INSERT INTO users VALUES (%s,%s)", [("admin","admin123"),("ram","ram123"),("sita","sita123")])
#     conn.commit()

# def login():
#     cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user.get(), pwd.get()))
#     result.config(text="Login Successful" if cursor.fetchone() else "Invalid Credentials")

# root = tk.Tk()
# root.title("Login System")

# tk.Label(root, text="Username").pack()
# user = tk.Entry(root)
# user.pack()

# tk.Label(root, text="Password").pack()
# pwd = tk.Entry(root, show="*")
# pwd.pack()

# tk.Button(root, text="Login", command=login).pack()
# result = tk.Label(root, text="")
# result.pack()

# root.mainloop()



#............................................................


# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("localhost", 9999))
# server.listen(1)
# print("Server waiting for connection...")

# conn, addr = server.accept()
# print(f"Connected to {addr}")
# conn.send("Welcome to Orchid College".encode())
# conn.close()
# server.close()




# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("localhost", 9999))
# message = client.recv(1024).decode()
# print(f"Message from server: {message}")
# client.close()



#.......................................................



import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 9998))
server.listen(1)
print("Server waiting for connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")
name = conn.recv(1024).decode()
conn.send(f"How are you {name} ?".encode())
conn.close()
server.close()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9998))
name = input("Enter student name: ")
client.send(name.encode())
response = client.recv(1024).decode()
print(f"Server response: {response}")
client.close()