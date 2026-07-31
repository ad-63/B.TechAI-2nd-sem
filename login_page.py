# dynamic login page 
from tkinter import *
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="instagram"
)
cursor = conn.cursor()

def login():
    username = username_input.get()
    password = password_entry.get()
    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(sql, (username, password))
    user = cursor.fetchone()

    if user:
        result.config(
            text="Login successful",
            fg="green"
        )
        
    else:
        result.config(
            text="Invalid username or password",
            fg="red"
        )

"""login page window in tkinter"""

window = Tk()
window.title("instagram login page")
window.geometry("300x400")  

Label(window, text="Username:").grid(row=0, column=0)
username_input = Entry(window)
username_input.grid(row=0, column=1)

Label(window, text="Password:").grid(row=1, column=0)
password_entry = Entry(window, show="*")
password_entry.grid(row=1, column=1)

Button(window, text="submit", command=login).grid(row=2, column=1)

result = Label(window, font=("Arial", 11), text="")
result.grid(row=3, column=0, columnspan=2)

window.mainloop()