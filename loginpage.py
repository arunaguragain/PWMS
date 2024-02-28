import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk 
import sqlite3

class PasswordManagerLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1600x1600')
        self.root.title("Password Management System")

        # Load logo image
        self.image = Image.open('./logo.png')
        self.img = ImageTk.PhotoImage(self.image)
        tk.Label(self.root, image=self.img, bg='white', width=950).place(x=2, y=2, height=800)
        
        # Set up login widgets
        self.create_login_widgets()

    def create_login_widgets(self):
        # Labels and Entry widgets for login
        tk.Label(self.root, text="Log in", font=("Arial", 50), fg="navyblue").place(x=1100, y=140)
        tk.Label(self.root, text="Username", font=("Arial", 30)).place(x=1000, y=250)
        self.username_entry = tk.Entry(self.root, width=40, bg="white", borderwidth=8)
        self.username_entry.place(x=1200, y=260, height=35)
        tk.Label(self.root, text="Password", font=("Arial", 30)).place(x=1000, y=350)
        self.password_entry = tk.Entry(self.root, width=40, bg="white", borderwidth=8, show="*")
        self.password_entry.place(x=1200, y=360, height=35)

        # Login button
        tk.Button(self.root, text="Log in", font=("Arial", 30), bg="light blue", command=self.login).place(x=1190, y=450)

        # Sign up option
        tk.Label(self.root, text="Don't have an account?", font=("Arial", 20)).place(x=1000, y=600)
        tk.Button(self.root, text="Sign up", font=("Arial", 20), bg="light blue", command=self.signup).place(x=1300, y=595)

        self.root.config(bg="white")
        self.root.iconphoto(True, self.img) 

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == '' or password == '':
           messagebox.showerror('Error', 'All Fields Are Required.')
        else:
           conn = sqlite3.connect("users.db")
           db = conn.cursor()
        
        
        db.execute("SELECT * FROM users WHERE email=? AND password=?", (username, password))

        user_data = db.fetchone()
        
        if user_data==None:
            messagebox.showerror('Error','Invalid username or password.')
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end') 
        else:
            messagebox.showinfo('Welcome','Login is Successful.')
           
        
            conn.close()
            root.destroy()
            import homepage


    
    def signup(self):
        # Placeholder function for sign up functionality
        print("Signing up...")
        root.destroy()
        import registration_page

# Create the main window
root = tk.Tk()

# Create and run the login page
login_page = PasswordManagerLogin(root)

# Start the Tkinter event loop
root.mainloop()


