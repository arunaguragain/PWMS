# import tkinter as tk
# import sqlite3

# def create_table():
#     # Connect to the database (creates if not exists)
#     conn = sqlite3.connect('example.db')
#     c = conn.cursor()
    
#     # Create a table
#     c.execute('''CREATE TABLE IF NOT EXISTS users
#                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    
#     # Commit changes and close connection
#     conn.commit()
#     conn.close()

# def insert_data(name, email):
#     # Connect to the database
#     conn = sqlite3.connect('example.db')
#     c = conn.cursor()
    
#     # Insert data into the table
#     c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    
#     # Commit changes and close connection
#     conn.commit()
#     conn.close()

# def main():
#     # Create the GUI
#     root = tk.Tk()
#     root.title("Database Example")
    
#     # Create the database table if it doesn't exist
#     create_table()
    
#     # Function to handle button click
#     def add_user():
#         name = name_entry.get()
#         email = email_entry.get()
#         insert_data(name, email)
#         status_label.config(text="User added successfully.")
    
#     # Entry fields
#     tk.Label(root, text="Name:").pack()
#     name_entry = tk.Entry(root)
#     name_entry.pack()
    
#     tk.Label(root, text="Email:").pack()
#     email_entry = tk.Entry(root)
#     email_entry.pack()
    
#     # Button to add user
#     add_button = tk.Button(root, text="Add User", command=add_user)
#     add_button.pack()
    
#     # Status label
#     status_label = tk.Label(root, text="")
#     status_label.pack()
    
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        
        self.create_database_connection()
        
        self.create_widgets()
        
    def create_database_connection(self):
        # Connect to MySQL database
        self.db_connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="password_manager"
        )
        self.db_cursor = self.db_connection.cursor()
        
    def create_widgets(self):
        # Label and Entry for account name
        self.lbl_account = tk.Label(self.master, text="Account:")
        self.lbl_account.grid(row=0, column=0, sticky="e")
        self.ent_account = tk.Entry(self.master)
        self.ent_account.grid(row=0, column=1)
        
        # Label and Entry for password
        self.lbl_password = tk.Label(self.master, text="Password:")
        self.lbl_password.grid(row=1, column=0, sticky="e")
        self.ent_password = tk.Entry(self.master, show="*")
        self.ent_password.grid(row=1, column=1)
        
        # Buttons
        self.btn_save = tk.Button(self.master, text="Save", command=self.save_password)
        self.btn_save.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.btn_retrieve = tk.Button(self.master, text="Retrieve", command=self.retrieve_password)
        self.btn_retrieve.grid(row=3, column=0, columnspan=2, pady=10)
    
    def save_password(self):
        account = self.ent_account.get()
        password = self.ent_password.get()
        
        if account and password:
            # Insert data into the MySQL table
            insert_query = "INSERT INTO passwords (account, password) VALUES (%s, %s)"
            data = (account, password)
            self.db_cursor.execute(insert_query, data)
            self.db_connection.commit()
            
            messagebox.showinfo("Success", "Password saved successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both account and password.")
    
    def retrieve_password(self):
        account = self.ent_account.get()
        
        if account:
            # Retrieve data from the MySQL table
            retrieve_query = "SELECT password FROM passwords WHERE account = %s"
            data = (account,)
            self.db_cursor.execute(retrieve_query, data)
            result = self.db_cursor.fetchone()
            
            if result:
                password = result[0]
                messagebox.showinfo("Password", f"The password for {account} is: {password}")
            else:
                messagebox.showerror("Error", "Account not found.")
            
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter an account name.")
    
    def clear_entries(self):
        self.ent_account.delete(0, tk.END)
        self.ent_password.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
