import tkinter as tk
from tkinter import ttk

class FAQPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        # FAQ Title
        ttk.Label(self, text="Help & Frequently Asked Questions", font=("Helvetica", 16, "bold")).pack(pady=10)

        # FAQ Content
        faq_content = [
            {"question": "How do I sign up", "answer": "To sign up, go to the registration page and follow the instructions."},
            {"question": "How to add passwords to my vault?", "answer": "Log in and navigate to the 'Add Password' section. Enter the required details and save."},
            {"question": "Updating my password.", "answer": "Go to 'Home page' click on the update button and follow the instruction."},
            {"question": "Is my data secure?", "answer": "Yes, your data is well secured."},
            {"question": "Instructions to generate passwords.", "answer": "You can generate passwords after clicking onto the 'Generate' button."},
            {"question": "Can i access my passwords without connecting to the internet??", "answer": "Yes, we can access the passwords offline too."},
            ]

        for item in faq_content:
            ttk.Label(self, text=item["question"], font=("Helvetica", 12, "bold")).pack(pady=5, anchor="w")
            ttk.Label(self, text=item["answer"], wraplength=500, justify="left").pack(pady=5, anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Management System - FAQ Page")
    faq_page = FAQPage(master=root)
    faq_page.mainloop()
