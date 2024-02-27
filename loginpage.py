import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk 

class PasswordManagerLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1600x1600')
        self.root.title("Password Management System")

        # Load logo image
        self.image = Image.open('C:/Users/User/OneDrive/Desktop/password management system/logo.png')
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

        # Check if both username and password are entered
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        # Dummy authentication (replace with your authentication logic)
        if self.authenticate(username, password):
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
            # Add logic to navigate to the main dashboard or another page here
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def authenticate(self, username, password):
        # Replace this with your actual authentication logic (e.g., database check, API call)
        # This is a dummy authentication for illustration purposes
        return username == "admin" and password == "password123"
    
    def signup(self):
        # Placeholder function for sign up functionality
        print("Signing up...")

# Create the main window
root = tk.Tk()

# Create and run the login page
login_page = PasswordManagerLogin(root)

# Start the Tkinter event loop
root.mainloop()


