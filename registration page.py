import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import sqlite3

def validate_email(email):
    # Regular expression for validating email format
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email)

def validate_password(password):
    # Password must contain at least one uppercase letter, one lowercase letter,
    # one digit, one special character, and have a minimum length of 8 characters
    return any(c.isupper() for c in password) and \
           any(c.islower() for c in password) and \
           any(c.isdigit() for c in password) and \
           any(c in r"!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for c in password) and \
           len(password) >= 8

def sign_in():
    name = e1.get()
    email = e2.get()
    password = e3.get()
    reentered_password = e4.get()

    # Validate empty fields
    if not (name and email and password and reentered_password):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Validate email format
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address format")
        return

    # Validate password
    if not validate_password(password):
        messagebox.showerror("Error", "Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long")
        return

    # Validate password match
    if password != reentered_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Check if user is already registered
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    if c.fetchone():
        messagebox.showinfo("Already Registered", "You are already registered")
    else:
        # Register user
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration Successful", "You are registered")

root = tk.Tk()
root.geometry('300x400')
root.title("Sign in")

# Labels and Entry widgets
tk.Label(root, text="Full Name", bg='light green', font=("Arial", 15)).place(x=20, y=35)
e1 = tk.Entry(root, width=40, bg="white")
e1.place(x=20, y=63, height=27)
tk.Label(root, text="E-mail Address", bg='light green', font=("Arial", 15)).place(x=20, y=100)
e2 = tk.Entry(root, width=40, bg="white")
e2.place(x=20, y=128, height=27)
tk.Label(root, text="Enter Password", bg='light green', font=("Arial", 15)).place(x=20, y=165)
e3 = tk.Entry(root, width=40, bg="white")
e3.place(x=20, y=193, height=27)
tk.Label(root, text="Re-enter Password", bg='light green', font=("Arial", 15)).place(x=20, y=230)
e4 = tk.Entry(root, width=40, bg="white")
e4.place(x=20, y=258, height=27)

# Sign in button
tk.Button(root, text="Sign in", bg="light blue", font=("Arial", 15), command=sign_in).place(x=100, y=310)

root.config(bg="light green")
root.title("PWMS")
image = Image.open("C:/Users/User/OneDrive/Desktop/password management system/logo.png") 
photo = ImageTk.PhotoImage(image)
root.iconphoto(True, photo) 
root.resizable(False, False)   
root.mainloop()
