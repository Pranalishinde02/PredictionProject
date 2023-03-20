from tkinter import *
import tkinter as tk
from PIL import Image ,ImageTk
from tkinter import messagebox as ms
from subprocess import call
import sqlite3

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("DETECTION")
root.configure(background="cyan2")
image2 = Image.open('1.png')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 
heading = tk.Label(root,text="Placement Predictive System",width=50,height=2,font=("Times New Roman",25,"italic"),bg="black",fg="white")
heading.place(x=200,y=0)

def DR():
    #root.destroy()
    call(["python","Login_Admin.py"])


def PT():
    #root.destroy()
    call(["python","Login.py"])


def PT_R():
    call(['python','Registration.py'])
    
def DR_R():
    call(['python','Registration_Admin.py'])
    
    
    
    
dr = tk.Button(root,text="Admin Login",command=DR,font=("Times new roman", 25, "bold"),bg="cyan2")
dr.place(x=100,y=100)


pt = tk.Button(root,text="Student Login",command=PT,font=("Times new roman", 25, "bold"),bg="cyan2")
pt.place(x=100,y=200)




dr_R = tk.Button(root,text="Admin Registration",command=DR_R,font=("Times new roman", 25, "bold"),bg="cyan2")
dr_R.place(x=100,y=300)


pt_R = tk.Button(root,text="Student Registration",command=PT_R,font=("Times new roman", 25, "bold"),bg="cyan2")
pt_R.place(x=100,y=400)



root.mainloop()