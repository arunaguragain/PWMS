from tkinter import*
from PIL import Image, ImageTk 
root= Tk()
root.geometry('1700x1600')
root.title("log in")
image= Image.open('logo.png')
img= ImageTk.PhotoImage(image)
Label(root, image=img, bg='white',width=950).place(x=2,y=2,height=800)
myLabel= Label(root, text="Log in",font=("Arial",50),fg="navyblue").place(x=1100,y=140)
name= Label(root,text="Username",font=("Arial",30)).place(x=1000,y=250)
e1= Entry(root, width=40,bg="white",borderwidth=8).place(x=1200,y=260,height=35)
password= Label(root,text="Password",font=("Arial",30)).place(x=1000,y=350)
e2= Entry(root,width=40,bg="white",borderwidth=8).place(x=1200,y=360,height=35)
submitButton= Button(root,text="Log in",font=("Arial",30),bg="light blue").place(x=1190,y=450)
myLabel= Label(root, text="Don't have an account?",font=("Arial",20),).place(x=1000,y=600)
submitButton= Button(root,text="Sign up",font=("Arial",20),bg="light blue").place(x=1300,y=595)
root.config(bg="white")
root.mainloop()