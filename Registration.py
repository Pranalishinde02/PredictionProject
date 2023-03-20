import tkinter as tk
#from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image , ImageTk
import re
window =tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="cyan2")
image2 = Image.open('img1.jpg')
image2 = image2.resize((700, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 
Fullname = tk.StringVar()
rollno = tk.IntVar()
department = tk.StringVar()
tenth_mark = tk.IntVar()
twetlth_mark = tk.IntVar()
diploma = tk.IntVar()
extra_skills =tk.StringVar()
id = tk.StringVar()
password =tk.StringVar()
password1=tk.StringVar()
#database code
db = sqlite3.connect('student.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS entry_new"
               "(Fullname TEXT, rollno TEXT, department TEXT, tenth_mark TEXT, twetlth_mark TEXT,diploma TEXT,extra_skills TEXT,id TEXT , password TEXT)")
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
    rno = rollno.get()
    dept = department.get()
    tenth = tenth_mark.get()
    twetlth = twetlth_mark.get()
    dip = diploma.get()
    extra_s = extra_skills.get()
    time = id.get()
    pwd = password.get()
    cnpwd=password1.get()

    with sqlite3.connect('student.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM entry_new WHERE id = ?')
    c.execute(find_user, [(id.get())])

    #else:
     #   ms.showinfo('Success!', 'Account Created Successfully !')

    #to check mail
    #validation
    if(fname.isdigit()or(fname=="")):
        ms.showinfo("Message","please enter valid name")
    elif(rno==""):
        ms.showinfo("Message","Please Enter Roll No")
    elif(dept==""):
        ms.showinfo("Message", "Please Enter valid Department Name")
    elif(tenth==""):
        ms.showinfo("Message", "Please Enter valid 10th Marks")
    elif(twetlth==""):
        ms.showinfo("Message", "Please Enter valid 12th Marks")
    elif(dip==""):
        ms.showinfo("Message", "Please Enter valid diploma Marks")
    elif(time==""):
        ms.showinfo("Message", "Please Enter valid ID")
    elif(c.fetchall()):
        ms.showerror('Error!', 'ID Taken Try a Diffrent One.')
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "Please Enter valid password")
    elif(extra_s==False):
        ms.showinfo("Message", "Please Enter At least one extra skills")
    elif(pwd!=cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('student.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO entry_new(Fullname, rollno, department, tenth_mark, twetlth_mark,diploma, extra_skills, id , password) VALUES(?,?,?,?,?,?,?,?)',
                       (fname, rno,dept, tenth, twetlth,dip,extra_s, time, pwd))
            
            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
           # window.destroy()
            window.destroy()
            from subprocess import call
            call(["python","Login.py"])
    



    
   
l1=tk.Label(window,text="Registration Form",font=("Times new roman", 15, "bold"),bg="cyan2",fg="blue")
l1.place(x=250, y=50)

#that is for label1 registration

l2 =tk.Label(window, text="Full Name :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l2.place(x=130, y=100)
t1 =tk.Entry(window, textvar=Fullname,width=20, font=('', 15))
t1.place(x=330, y=100)
# that is for label 2 (full name)


l3 =tk.Label(window, text="Roll No :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l3.place(x=130, y=150)
t2 =tk.Entry(window, textvar=rollno,width=20, font=('', 15))
t2.place(x=330, y=150)
#that is for label 3(address)


#that is for label 4(blood group)

l5 =tk.Label(window, text="Department :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l5.place(x=130, y=200)
t4 =tk.Entry(window, textvar=department,width=20, font=('', 15))
t4.place(x=330, y=200)
#that is for email address

l6 =tk.Label(window, text="10th Marks :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l6.place(x=130, y=250)
t5 =tk.Entry(window, textvar= tenth_mark,width=20, font=('', 15))
t5.place(x=330, y=250)
#phone number
l7 =tk.Label(window, text="12th Marks :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l7.place(x=130, y=300)
t5 =tk.Entry(window, textvar= twetlth_mark,width=20, font=('', 15))
t5.place(x=330, y=300)
#diploma
l11 =tk.Label(window, text="Diploma Marks :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l11.place(x=130, y=350)
t11 =tk.Entry(window, textvar= diploma,width=20, font=('', 15))
t11.place(x=330, y=350)


l8 =tk.Label(window, text="Extra Skills :", width=12, font=("Times new roman", 15, "bold"),bg="cyan2")
l8.place(x=130, y=400)
t6 =tk.Entry(window, textvar=extra_skills,width=20, font=('', 15))
t6.place(x=330, y=400)

l4 =tk.Label(window, text="ID :", width=12,font=("Times new roman", 15, "bold"),bg="cyan2")
l4.place(x=130, y=450)
t3 =tk.Entry(window, textvar=id,width=20, font=('', 15))
t3.place(x=330, y=450)

l9 =tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"),bg="cyan2")
l9.place(x=130, y=500)
t9 =tk.Entry(window, textvar=password,width=20, font=('', 15),show="*")
t9.place(x=330, y=500)

l10 =tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"),bg="cyan2")
l10.place(x=130, y=550)
t10 =tk.Entry(window, textvar=password1,width=20, font=('', 15),show="*")
t10.place(x=330, y=550)

btn=tk.Button(window, text="Register", bg ="dark green", fg = "white", width=15, height=2, command=insert)
btn.place(x=250, y=600)
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