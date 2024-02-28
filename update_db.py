import tkinter as tk
from tkinter import messagebox
import sqlite3

def update_password():
    # Connect to the database
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    # Get values from entry widgets
    website = website_entry.get()
    username = username_entry.get()
    new_password = new_password_entry.get()

    # Update user's password
    update_query = """
        UPDATE passwords
        SET password = ?
        WHERE website = ? AND username = ?
    """
    cursor.execute(update_query, (new_password, website, username))
    conn.commit()

    messagebox.showinfo("Success", "Password updated successfully.")

    # Close the connection
    conn.close()

# Create Tkinter window
window = tk.Tk()
window.title("Password Management System - Update Password")

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

# New password entry
new_password_label = tk.Label(window, text="New Password:")
new_password_label.grid(row=2, column=0, padx=5, pady=5)
new_password_entry = tk.Entry(window, show="*")
new_password_entry.grid(row=2, column=1, padx=5, pady=5)

# Update button
update_button = tk.Button(window, text="Update Password", command=update_password)
update_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
window.mainloop()
