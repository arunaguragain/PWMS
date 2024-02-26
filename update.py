import tkinter as tk
import sqlite3

window= tk.Tk()
window.geometry('300x400')
window.title("Password Management System Update")
def open_update_window():
    update_window = tk.Toplevel(window)
    update_window.title("Update Password")
    update_window.geometry("400x200")

    # Labels and Entry fields
    website_label = tk.Label(update_window, text="Website:", font=('Arial', 12))
    website_label.grid(row=0, column=0)
    website_entry = tk.Entry(update_window, font=('Arial', 12))
    website_entry.grid(row=0, column=1)

    username_label = tk.Label(update_window, text="Username:", font=('Arial', 12))
    username_label.grid(row=1, column=0)
    username_entry = tk.Entry(update_window, font=('Arial', 12))
    username_entry.grid(row=1, column=1)

    password_label = tk.Label(update_window, text="Password:", font=('Arial', 12))
    password_label.grid(row=2, column=0)
    password_entry = tk.Entry(update_window, font=('Arial', 12))
    password_entry.grid(row=2, column=1)

    # Update button
    def update_details():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # Implement your update logic here
        # For example, you can call a function similar to update_password() from your main window code
        # Make sure to handle errors and provide appropriate feedback

    update_button = tk.Button(update_window, text="Update", font=('Arial', 12), command=update_details)
    update_button.grid(row=3, columnspan=2)

# Example usage
update_button = tk.Button(window, text="Update Password", font=('Arial', 12), command=open_update_window)
update_button.place(x=950, y=405, height=60)

window.mainloop()