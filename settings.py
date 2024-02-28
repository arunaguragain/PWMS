import tkinter as tk
from tkinter import ttk, messagebox

class AboutPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("About.TLabel", font=("Helvetica", 14))

        self.configure(bg='light blue')  # Set background color
        
        ttk.Label(self, text="About Our Password Management System", style="About.TLabel", background='light blue').pack()

        ttk.Label(self, text="Our Mission: [To reduce the stress of having to remember numerous passwords]", style="About.TLabel", background='light blue').pack()
        ttk.Label(self, text="Features: [Storing passwords and generating passwords]", style="About.TLabel", background='light blue').pack()
        ttk.Label(self, text="Our Team: [Aruna Guragain, Samikshya Baniya, Shreeya Paudel, Aayuska Adhikari]", style="About.TLabel", background='light blue').pack()
        ttk.Label(self, text="Contact Us: [guragainaruna@gmail.com, samekshya03@gmail.com, shreeya.paudel.8e@gmail.com, aayuskaadhikari1@gmail.com]", style="About.TLabel", background='light blue').pack()

class FAQPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("FAQ.TLabel", font=("Helvetica", 12))

        self.configure(bg='light blue')  # Set background color

        ttk.Label(self, text="Help & Frequently Asked Questions", style="FAQ.TLabel", background='light blue').pack()

        faq_content = [
            {"question": "How do I sign up", "answer": "To sign up, go to the registration page and follow the instructions."},
            {"question": "How to add passwords to my vault?", "answer": "Log in and navigate to the 'Add Password' section. Enter the required details and save."},
            {"question": "Updating my password.", "answer": "Go to 'Home page' click on the update button and follow the instruction."},
            {"question": "Is my data secure?", "answer": "Yes, your data is well secured."},
            {"question": "Instructions to generate passwords.", "answer": "You can generate passwords after clicking onto the 'Generate' button."},
            {"question": "Can i access my passwords without connecting to the internet?", "answer": "Yes, we can access the passwords offline too."},
        ]

        y_position = 70  # Initial y position for placement

        for item in faq_content:
            ttk.Label(self, text=item["question"], style="FAQ.TLabel", background='light blue').place(x=10, y=y_position)
            ttk.Label(self, text=item["answer"], wraplength=500, justify="left", style="FAQ.TLabel", background='light blue').place(x=10, y=y_position+20)
            y_position += 50  # Increase y position for next item

class SettingsPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Settings.TLabel", font=("Helvetica", 16))

        self.configure(bg='light blue')  # Set background color

        ttk.Label(self, text="Settings", style="Settings.TLabel", background='light blue').pack()

        profile_button = ttk.Button(self, text="Profile", command=self.view_profile)
        profile_button.pack()

        about_button = ttk.Button(self, text="About", command=self.view_about)
        about_button.pack()

        help_button = ttk.Button(self, text="Help & FAQs", command=self.view_help)
        help_button.pack()

        logout_button = ttk.Button(self, text="Logout", command=self.logout)
        logout_button.pack()

    def view_profile(self):
        # Add functionality to view the user's profile
        pass

    def view_about(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("About")
        about_page = AboutPage(master=about_window)

    def view_help(self):
        help_window = tk.Toplevel(self.master)
        help_window.title("Help & FAQs")
        faq_page = FAQPage(master=help_window)

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            # Add logout functionality here
            # For example, you can close the main window and open a login window
            self.master.destroy()  # Close the main window
            import loginpage
            



root = tk.Tk()
root.title("Password Management System - Settings")
root.geometry("1600x1600")  # Set window size
settings_page = SettingsPage(master=root)
settings_page.mainloop()

