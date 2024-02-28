import tkinter as tk
from tkinter import messagebox
import sqlite3

def register_user():
    # Connect to the database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Get values from entry widgets
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Insert new user into the database
    insert_query = "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)"
    cursor.execute(insert_query, (website, username, password))
    conn.commit()

    messagebox.showinfo("Success", "Registration successful!")

    # Close the connection
    conn.close()

# Create Tkinter window
window = tk.Tk()
window.title("Password Management System - Registration")

# Website entry
website_label = tk.Label(window, text="Website:")
website_label.grid(row=0, column=0, padx=5, pady=5)
website_entry = tk.Entry(window)
website_entry.grid(row=0, column=1, padx=5, pady=5)

# Username entry
username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, padx=5, pady=5)

# Password entry
password_label = tk.Label(window, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Register button
register_button = tk.Button(window, text="Register", command=register_user)
register_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()
