import tkinter as tk
from tkinter import messagebox
import sqlite3

window=tk.Tk()
window.geometry('300x400')
window.title("Password Management System Update")
window.configure(bg='light blue')

def open_update_window():
    update_window = tk.Toplevel(window)
    update_window.title("Update")
    update_window.geometry("400x400")
    update_window.configure(bg='light blue')

    # Labels and Entry fields
    website_label = tk.Label(update_window, text="Website:", font=('Arial', 15), bg='light blue').place(x=45,y=10)
    website_entry = tk.Entry(update_window, font=('Arial', 15))
    website_entry.place(x=45,y=40)

    username_label = tk.Label(update_window, text="Username:", font=('Arial', 15), bg='light blue').place(x=45,y=80)
    username_entry = tk.Entry(update_window, font=('Arial', 15))
    username_entry.place(x=45,y=120)

    password_label = tk.Label(update_window, text="Password:", font=('Arial', 15), bg='light blue').place(x=45,y=160)
    password_entry = tk.Entry(update_window, font=('Arial', 15))
    password_entry.place(x=45,y=200)

    # Update button
    def update_details():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        if not website or not username or not password:
            messagebox.showerror("Error", "Please fill in all the fields.")
        else:
            # Implement your update logic here
            # For example, you can call a function similar to update_password() from your main window code
            # Make sure to handle errors and provide appropriate feedback
            # For now, let's just show a message box saying the information has been updated
            messagebox.showinfo("Success", "Your information has been updated.")

    update_button = tk.Button(update_window, text="Update", font=('Arial', 18), command=update_details).place(x=100,y=260)
    window.resizable(False, False)

# Example usage
update_button = tk.Button(window, text="Update", font=('Arial', 18), command=open_update_window)
update_button.place(x=950, y=405, height=60)

window.mainloop()
