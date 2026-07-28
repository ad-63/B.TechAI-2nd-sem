# dynamic login page 
from tkinter import *


window=Tk()
window.title("instagram login page")
window.geometry("300x400")

label1=Label(window, text="Username:")
label1.grid(row=0, column=0)
username_input=Entry(window)
username_input.grid(row=0, column=1)

label2=Label(window, text="Password:")
label2.grid(row=1, column=0)
password_input=Entry(window)
password_input.grid(row=1, column=1)

button=Button(window, text="Login")
button.grid(row=2, column=1)
window.mainloop()