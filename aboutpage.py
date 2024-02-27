"""About Page"""
import tkinter as tk

class AboutPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="About Our Password Management System", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.mission_label = tk.Label(self, text="Our Mission: [To reduce the stress of having to remember numerous passwords]")
        self.mission_label.pack()

        self.features_label = tk.Label(self, text="Features: [Storing passwords and generating passwords]")
        self.features_label.pack()

        self.team_label = tk.Label(self, text="Our Team: [Aruna Guragain, Samikshya Baniya, Shreeya Paudel, Aayuska Adhikari]")
        self.team_label.pack()

        self.contact_label = tk.Label(self, text="Contact Us: [guragainaruna@gmail.com, samekshya03@gmail.com, shreeya.paudel.8e@gmail.com, aayuskaadhikari1@gmail.com]")
        self.contact_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AboutPage(master=root)
    app.mainloop()
