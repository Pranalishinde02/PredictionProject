from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from joblib import dump , load
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox as ms

root = tk.Tk()
w , h = root.winfo_screenwidth() , root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.title("Placement Prediction System")
root.configure(background="cyan2")


#
image2 = Image.open('bg.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 


# frame_alpr = tk.LabelFrame(root, text="output", width=800, height=100, bd=5, font=('times', 14, ' bold '),bg="grey")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=400, y=600)

#
def check_value():
    en6.get()
    name_here = en6.get()
    abc = pd.read_csv(r"Test.csv")
    abc1 = abc[abc['Seat No']==str(name_here)]
    print(abc1['Avrage'].values[0])
    #abc1 = abc[abc['Name']=='BABAR AJAY DEEPAK']
    if int(abc1['Avrage'].values[0])>int(60):
        print("YES")
        

        frame_alpr = tk.LabelFrame(root, text="output", width=800, height=350, bd=5, font=('times', 14, ' bold '),bg="white")
        frame_alpr.grid(row=0, column=0, sticky='nw')
        frame_alpr.place(x=400, y=300)
        eligibility = tk.Label(frame_alpr,text ="You are Eligible :",font=('Times New Roman',15,'italic'),width=27,bg='cyan2',fg='black')
        eligibility.place(x=10,y=5)
        e1 = abc1['10th'].values[0]
        e2 = abc1['12th'].values[0]
        e3 = abc1['1st_year'].values[0]
        e4 = abc1['2nd_year'].values[0]
        e5 = abc1['3rd_year'].values[0]


        from joblib import load
        model = load(r"SVM_MODEL.joblib")
        #model.predict([[76,69,74,60,90]])[0]
        output = model.predict([[e1,e2,e3,e4,e5]])
        print(output)
        if output[0]==0:
            result = "Data Base Developer\nRedHat\nVM_Ware\nMariaDB\nSonicks\nComentum\nWBD\nGirnarsoft"
            print("Data Base Developer")
        if output[0]==1:
            result = "Networking Engineer\nCISCO IND\nIBM IND\nTCS\nL&T\nAT&T\nBHARTI AIRTEL"
            print("Networking Engineer")
        if output[0]==2:
            result = "System Architect\nCISCO SYSTEM\nSIEMENS\nINNOVATURE LABS\nNVIDIA\nCAPGEMINI\nNOKIA"
            print("System Architect")
        if output[0]==3:
            result = "Software Developer\nTECH MAHINDRA\nHCL TECH\nMINDTREE\nHEXAWARE\nDOTSQUARES"
            print("Software Developer")
        a=result
            #return a
        eligibility = tk.Label(frame_alpr,text =str(a),font=('Times New Roman',18,'italic'),width=27,bg='cyan2',fg='black')
        eligibility.place(x=10,y=50)
       
        
        
    else:
        print("NO")
        

        frame_alpr = tk.LabelFrame(root, text="output", width=800, height=350, bd=5, font=('times', 14, ' bold '),bg="white")
        frame_alpr.grid(row=0, column=0, sticky='nw')
        frame_alpr.place(x=400, y=300)
        eligibility = tk.Label(frame_alpr,text ="You are NOT Eligible ",font=('Times New Roman',15,'italic'),width=27,bg='cyan2',fg='black')
        eligibility.place(x=30,y=10)
       
        
   

en6_L = tk.Label(root,text="Enter Your Seat No",font=('Times New Roman',18),width=30,bg='cyan2',fg='black')
en6_L.place(x=450,y=100)

en6  = tk.Entry(root,width=30,bg="white",fg="red")
en6.place(x=550,y=150)


ele = tk.Button(root,text="Prediction",command=check_value,font=('Times New Roman',12,'italic'),width=15,bg='black',fg='linen')
ele.place(x=550,y=250)

root.mainloop()
"""
import random


random.randint(50,90)


import random 
  
# Function to generate 
# and append them  
# start = starting range, 
# end = ending range 
# num = number of  
# elements needs to be appended 
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
  
# Driver Code 
num =172
start = 50
end = 90
print(Rand(start, end, num)) 

here = Rand(start, end, num)

225-53
"""


