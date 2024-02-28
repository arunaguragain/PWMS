import tkinter as tk
from tkinter import messagebox

def register():
    full_name = full_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    re_password = re_password_entry.get()
    
    # Validate password and re-enter password
    if password != re_password:
        messagebox.showerror("Error", "Passwords do not match")
        return
    
    # Insert code to save the registration details to a database here
    
    # Show success message
    messagebox.showinfo("Success", "Registration successful")

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Create labels
full_name_label = tk.Label(root, text="Full Name:")
full_name_label.grid(row=0, column=0, padx=5, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)

re_password_label = tk.Label(root, text="Re-enter Password:")
re_password_label.grid(row=3, column=0, padx=5, pady=5)

# Create entry fields
full_name_entry = tk.Entry(root)
full_name_entry.grid(row=0, column=1, padx=5, pady=5)

email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

re_password_entry = tk.Entry(root, show="*")
re_password_entry.grid(row=3, column=1, padx=5, pady=5)

# Create register button
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI
root.mainloop()
