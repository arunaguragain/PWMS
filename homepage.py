import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
import string
from PIL import Image, ImageTk

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", (website, username, password))
    conn.commit()
    conn.close()

    clear_fields()
    display_website_list()

def search_password():
    website = website_entry.get()

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords WHERE website=?", (website,))
    result = c.fetchone()
    conn.close()

    if result:
      website_list.selection_clear(0, tk.END)
      index = website_list.get(0, tk.END).index(result[0])
      website_list.selection_set(index)
      website_list.activate(index)
    else:
        messagebox.showinfo("Info", f"No details for {website} exists.")


        
def delete_password():
    website = website_entry.get()

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE website=?", (website,))
    conn.commit()
    conn.close()

    response = messagebox.askokcancel("Confirmation", f"Do you want to delete {website} details?")
    if response:
        clear_fields()
        display_website_list()


def update_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("UPDATE passwords SET username=?, password=? WHERE website=?", (username, password, website))
    conn.commit()
    conn.close()

    messagebox.showinfo("Info", f"Updated {website} details.")
    clear_fields()
    display_website_list()

def clear_fields():
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)



def share_password():
    selected_website = website_list.get(tk.ACTIVE)
    if not selected_website:
        messagebox.showwarning("Warning", "Please select a website from the list.")
        return

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords WHERE website=?", (selected_website,))
    result = c.fetchone()
    conn.close()

    if result:
        username, password = result[1], result[2]
        messagebox.showinfo("Share Password", f"You can share the username and password for {selected_website}:\nUsername: {username}\nPassword: {password}")
    else:
        messagebox.showwarning("Warning", "No details found for the selected website.")



def read_password():
    selected_website = website_list.get(tk.ACTIVE)
    if not selected_website:
        messagebox.showwarning("Warning", "Please select a website from the list.")
        return

    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords WHERE website=?", (selected_website,))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Username and Password", f"Website: {result[0]}\nUsername: {result[1]}\nPassword: {result[2]}")
    else:
        messagebox.showwarning("Warning", "No details found for the selected website.")

def display_website_list():
    website_list.delete(0, tk.END)
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT website FROM passwords")
    records = c.fetchall()
    conn.close()

    for record in records:
        website_list.insert(tk.END, record[0])

def on_website_select(event):
    selected_website = website_list.get(tk.ACTIVE)
    website_entry.delete(0, tk.END)
    website_entry.insert(0, selected_website)
    
# GUI setup
window = tk.Tk()
window.title("Password Management System")
window.geometry("1600x1600")

image = Image.open("C:/Users/User/OneDrive/Desktop/password management system/logo.png") 
photo = ImageTk.PhotoImage(image)
window.iconphoto(True, photo)

website_label = tk.Label(window, text="Site/App",font=('Arial',35))
website_label.grid(row=0, column=0)
website_entry = tk.Entry(window,fg='Dark blue',width=22,font=('Arial',15))
website_entry.place(x=220, y=18,height=32)
website_entry.focus()

username_label = tk.Label(window, text="Username",font=('Arial',35))
username_label.place(x=900, y=0)
username_entry = tk.Entry(window,fg='Dark green',width=22,font=('Arial',15))
username_entry.place(x=1140, y=18,height=32)

password_label = tk.Label(window, text="Password",font=('Arial',35))
password_label.place(x=900, y=55)
password_entry = tk.Entry(window,fg='Dark green',width=22,font=('Arial',15))
password_entry.place(x=1140, y=75,height=32)


generate_button = tk.Button(window, width=10,font=('Arial',30), bg='violet' ,text="Generate\nPassword", command=generate_password)
generate_button.place(x=950, y=645,height=85)

Create_button = tk.Button(window,width=10,font=('Arial',30), bg='royal blue', text="Create", command=save_password)
Create_button.place(x=950, y=165,height=60)

search_button = tk.Button(window,width=10,font=('Arial',30), bg='light blue', text="Search", command=search_password)
search_button.place(x=950,y=565,height=60)

delete_button = tk.Button(window,width=10,font=('Arial',30), bg='yellow', text="Delete", command=delete_password)
delete_button.place(x=950, y=405,height=60)

update_button = tk.Button(window, width=10,font=('Arial',30), bg='hot pink', text="Update", command=update_password)
update_button.place(x=950, y=325,height=60)

Share_button = tk.Button(window,width=10,font=('Arial',30), bg='light pink', text="Share", command=share_password)
Share_button.place(x=950,y=485,height=60)

read_button = tk.Button(window,width=10,font=('Arial',30), bg='light green', text="Read", command=read_password)
read_button.place(x=950, y=245,height=60)

website_list_label = tk.Label(window,width=18,font=('Arial',30), text="Websites/Applications")
website_list_label.place(x=0,y=110)

website_list = tk.Listbox(window,font=('Arial',30) ,width=38, height=35)
website_list.place(x=10,y=165)
website_list.bind("<<ListboxSelect>>", on_website_select)

display_website_list()

def open_settings():
    pass

setting_icon = tk.PhotoImage(file="C:/Users/User/OneDrive/Desktop/password management system/password_4370811.png")
setting_button = tk.Button(window,width=50,image=setting_icon, command=open_settings)
setting_button.place(x=1400,y=700,height=50)



window.mainloop()

 
