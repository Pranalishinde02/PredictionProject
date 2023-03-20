import tkinter as tk
#from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image , ImageTk
import re
window =tk.Tk()
window.geometry("700x500")
window.title("REGISTRATION FORM")
window.configure(background="cyan2")
image2 = Image.open('img1.jpg')
image2 = image2.resize((700, 500), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 
univer_id = tk.StringVar()
Fullname = tk.StringVar()
department = tk.StringVar()
id = tk.StringVar()

password =tk.StringVar()
password1=tk.StringVar()
#database code
db = sqlite3.connect('student.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS entry_admin"
               "(University_id TEXT,Fullname TEXT, department TEXT, id TEXT,password TEXT)")
db.commit()

def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 
def insert():

    fname = Fullname.get()
    u_id = univer_id.get()
    dept = department.get()
    ids = id.get()
    pwd = password.get()
    cnpwd=password1.get()

    with sqlite3.connect('student.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM entry_admin WHERE id = ?')
    c.execute(find_user, [(id.get())])

    #validation
    if(fname.isdigit()or(fname=="")):
        ms.showinfo("Message","please enter valid name")
    elif(u_id==""):
        ms.showinfo("Message","Please Enter University ID")
    elif(ids==""):
        ms.showinfo("Message","Please Enter ID")
    elif(c.fetchall()):
        ms.showerror('Error!', 'ID Taken Try a Diffrent One.')
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "Please Enter valid password")
    elif(dept==""):
        ms.showinfo("Message", "Please Enter Department Name")
    elif(pwd!=cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('student.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entry_admin(University_id,Fullname, department, id,password) VALUES(?,?,?,?,?)',
                       (u_id,fname,dept,ids,pwd))
            
            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
           # window.destroy()
            window.destroy()
            from subprocess import call
            call(["python","Login_Admin.py"])
    



    
   
l1=tk.Label(window,text="Registration Form",font=("Times new roman", 15, "bold"),bg="cyan2",fg="blue")
l1.place(x=250, y=50)

#that is for label1 registration

l3 =tk.Label(window, text="University ID :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l3.place(x=130, y=100)
t2 =tk.Entry(window, textvar=univer_id,width=20, font=('', 15))
t2.place(x=330, y=100)

l2 =tk.Label(window, text="Full Name :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l2.place(x=130, y=150)
t1 =tk.Entry(window, textvar=Fullname,width=20, font=('', 15))
t1.place(x=330, y=150)

l5 =tk.Label(window, text="Department :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l5.place(x=130, y=200)
t4 =tk.Entry(window, textvar=department,width=20, font=('', 15))
t4.place(x=330, y=200)
#that is for email address

l6 =tk.Label(window, text="ID :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l6.place(x=130, y=250)
t5 =tk.Entry(window, textvar= id,width=20, font=('', 15))
t5.place(x=330, y=250)

l9 =tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"),bg="cyan2")
l9.place(x=130, y=300)
t9 =tk.Entry(window, textvar=password,width=20, font=('', 15),show="*")
t9.place(x=330, y=300)

l10 =tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"),bg="cyan2")
l10.place(x=130, y=350)
t10 =tk.Entry(window, textvar=password1,width=20, font=('', 15),show="*")
t10.place(x=330, y=350)

btn=tk.Button(window, text="Register", bg ="dark green", fg = "white", width=15, height=2, command=insert)
btn.place(x=250, y=400)
#tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
#tologin.place(x=330, y=600)
window.mainloop()


"""
# Password validation in Python 
# using naive method 

# Function to validate the password 
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

# Main method 
def main(): 
	passwd = 'Geek12@'
	
	if (password_check(passwd)): 
		print("Password is valid") 
	else: 
		print("Invalid Password !!") 

(password_check("Omkar123"))
# Driver Code		 
if __name__ == '__main__': 
	main() 
"""