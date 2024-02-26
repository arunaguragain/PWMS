from tkinter import*
from PIL import Image, ImageTk
import re
from tkinter import messagebox
def validate_email(email):
    # Regular expression for validating email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_password(password, reentered_password):
    return password == reentered_password

def sign_in():
    name = e1.get()
    email = e2.get()
    password = e3.get()
    reentered_password = e4.get()

    # Validate email format
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address format")
        return

    # Validate password match
    if not validate_password(password, reentered_password):
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Placeholder functionality for sign-in
    print("Signing in...")
root= Tk()
root.geometry('300x400')
root.title("sign in")
name= Label(root,text="Full Name",bg='light green',font=("Arial",15)).place(x=20,y=35)
e1= Entry(root, width=40,bg="white").place(x=20,y=63,height=27)
email= Label(root,text="E-mail Address", bg='light green',font=("Arial",15)).place(x=20,y=100)
e2= Entry(root,width=40,bg="white").place(x=20,y=128,height=27)
enterpassword= Label(root,text="Enter Password", bg='light green',font=("Arial",15)).place(x=20,y=165)
e3= Entry(root,width=40,bg="white").place(x=20,y=193,height=27)
enterpassword= Label(root,text="Re-enter Password", bg='light green',font=("Arial",15)).place(x=20,y=230)
e4= Entry(root,width=40,bg="white").place(x=20,y=258,height=27)
submitButton= Button(root,text="sign in",bg="light blue",font=("Arial",15),command=sign_in).place(x=100,y=310)
root.config(bg="light green")
root.title("PWMS")
image = Image.open("C:/Users/User/OneDrive/Desktop/password management system/logo.png") 
photo = ImageTk.PhotoImage(image)
root.iconphoto(True, photo) 
root.resizable(False,False)   
root.mainloop()

