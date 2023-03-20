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
import matplotlib.pyplot as plt
import sqlite3
from tkinter import messagebox as ms

root = tk.Tk()
w , h = root.winfo_screenwidth() , root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.title("Placement Prediction System")

img = Image.open(r"E:\Placement_Prediction_System\bg.jpg")

bg = img.resize((w,h),Image.ANTIALIAS)

bg_img = ImageTk.PhotoImage(bg)

bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=0)

heading = tk.Label(root,text="Placement Predictive System",width=100,height=2,font=("Times New Roman",21,"italic"),bg="black",fg="white")
heading.place(x=0,y=0)



""" Sample """


sample = test = pd.read_csv("E:\Placement_Prediction_System/Sample.csv")

sample["Role"] = le.fit_transform(sample["Role"])
sample.dropna()
a = sample.drop(["Seat No","Name","Role"],axis=1)
b = sample["Role"]

a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.20)


# """ Decision Tree """

# def DT():
#     DT_model = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=3, min_samples_leaf=5)   
        
#     DT_model.fit(a_train, b_train.values.ravel())
    
#     DT_p = DT_model.predict(a_test)
    
#     print("DT Classification Report : ", (classification_report(b_test, DT_p)))
#     repo = classification_report(b_test, DT_p)
#     label2 = tk.Label(root,text =str(repo),width=50,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label2.place(x=205,y=100)

# """ Naivey Bayes """

# def NB():
#     NB_model = GaussianNB()
#     NB_model.fit(a_train, b_train.values.ravel())
        
#     NB_p = NB_model.predict(a_test)
    
#     print("NB Classification Report : ", (classification_report(b_test, NB_p)))
#     repo = classification_report(b_test, NB_p)
#     label2 = tk.Label(root,text =str(repo),width=50,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label2.place(x=205,y=100)

# """ KNN """

# def KNN():
#     from sklearn.neighbors import KNeighborsClassifier 
    
#     KNN_model = KNeighborsClassifier(n_neighbors=4,metric = 'minkowski', p = 2)
    
#     KNN_model.fit(a_train,b_train)
    
    
#     KNN_p = KNN_model.predict(a_test)
    
#     print("KNN Classification Report : ", (classification_report(b_test, KNN_p)))
#     repo = classification_report(b_test, KNN_p)
#     label2 = tk.Label(root,text =str(repo),width=50,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
#     label2.place(x=205,y=100)


""" SVM """
# def classification_report_csv(report):
#         report_data = []
#         lines = report.split('\n')
#         for line in lines[2:-3]:
#             row = {}
#             row_data = line.split('  ')
#             #row['class'] = row_data[0]
#             row['precision'] = row_data[0]
#             row['recall'] = row_data[1]
#             row['f1_score'] = row_data[2]
#             row['support'] = row_data[3]
#             report_data.append(row)
#         dataframe = pd.DataFrame.from_dict(report_data)
#         dataframe.to_csv('classification_report.csv', index = False)


def SVM():
    
    #from sklearn.svm import SVC
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(a_train, b_train)
    
    b_pred = svcclassifier.predict(a_test)
    print(b_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(b_test, b_pred)))
    print("Accuracy : ",accuracy_score(b_test,b_pred)*100)
    accuracy = accuracy_score(b_test, b_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(b_test, b_pred) * 100)
    print("Accuracy:",accuracy_score(b_test, b_pred))
    #print("Precision:",precision_score(b_test, b_pred))
    #print("Recall:",recall_score(b_test, b_pred))
    report = classification_report(b_test, b_pred)
    # report_data = []
    # lines = report.split('\n')
    # for line in lines[2:(len(lines) - 4)]:
    #     row = {}
    #     row_data = line.split('      ')
    #    # row['class'] = row_data[0]
    #     row['precision'] = row_data[0]
    #     row['recall'] = row_data[1]
    #     row['f1_score'] = row_data[2]
    #     row['support'] = row_data[3]
    #     report_data.append(row)
    # dataframe = pd.DataFrame.from_dict(report_data)
    # dataframe.to_csv('classification_report.csv', index = False)
    
    
    #label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    #label4.place(x=205,y=200)
    image2 = Image.open("Capture.png")
    image2 = image2.resize((500,350), Image.ANTIALIAS)

    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=350, y=120) 
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=350,y=480)
    from joblib import dump
    dump (svcclassifier,"SVM_MODEL.joblib")
    print("Model saved as SVM_MODEL.joblib")

   #  import matplotlib.pyplot as plt
   #  #list all data in svcclassifier
   #  print(svcclassifier.svcclassifier.keys())
   # # summarize history for accuracy
   #  plt.plot(svcclassifier.svcclassifier['ACC'])
   #  plt.plot(svcclassifier.svcclassifier['repo'])
   #  plt.title('model accuracy')
   #  plt.ylabel('accuracy')
   #  plt.xlabel('epoch')
   #  plt.legend(['train', 'test'], loc='upper left')
   #  plt.show()
   # # summarize history for loss
   #  plt.plot(svcclassifier.svcclassifier['loss'])
   #  plt.plot(svcclassifier.svcclassifier['val_loss'])
   #  plt.title('model loss')
   #  plt.ylabel('loss')
   #  plt.xlabel('epoch')
   #  plt.legend(['train', 'test'], loc='upper left')
   #  plt.show()
# def PRED():
#     SVM_model = load(r"E:\Placement_Prediction_System\DND_Model\SVM_85.joblib")
#     g = pd.read_csv(r"E:\Placement_Prediction_System\Test.csv")
#     g.dropna()
#     h = g.drop(["Role","Seat No","Name","SOFT SKILLS","1st_year_lab","2nd_year_lab","Height"],axis=1)
    
#     j = SVM_model.predict(h)
    
    


#     test = pd.read_csv("E:\Placement_Prediction_System/Test.csv")
#     test.dropna()
#     trial = test.drop(["Seat No","Name","1st_year_lab","2nd_year_lab","SOFT SKILLS"],axis=1)


def NEW_COM():
    new_entry = tk.Toplevel()
    Exdate = tk.StringVar()
    
    new_entry.geometry("500x200+300+100")
    new_entry.title("Add New Drive")
    new_entry.configure(background='cyan')
    
    date= DateEntry(new_entry, width=25, year=2020, month=6, day=22,background='darkblue', foreground='white', borderwidth=2, textvariable =Exdate)
    date.place(x=5,y=5)
    
    c_name = tk.Label(new_entry,text='Company Name',font=('Times New Roman',10),width=14,bg='black',fg='linen')
    c_name.place(x=5,y=30)
    name_entry = tk.Entry(new_entry,font=('Times New Roman',10),width=20,bg='white',fg='red')
    name_entry.place(x=120,y=30)
    
    criteria = tk.Label(new_entry,text='Criteria',font=('Times New Roman',10),width=14,bg='black',fg='linen')
    criteria.place(x=5,y=60)
    criteria_entry = tk.Entry(new_entry,width=20,bg='white',fg='red')
    criteria_entry.place(x=120,y=60)
    
    def into():
        conn = sqlite3.connect('DRIVE.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        c.execute("CREATE TABLE IF NOT EXISTS COMPANY""(company TEXT,date TEXT, criteria TEXT)")
        date_value = Exdate.get()
        company_value = name_entry.get()
        criteria_value = criteria_entry.get()
        c.execute("INSERT INTO COMPANY(company,date,criteria)VALUES(?,?,?)",(company_value,date_value,criteria_value))
        
        conn.commit()
        conn.close()
        
        ms.showinfo('Success!', 'Company Drive Added Successfully !')
    
        
        
        abc = pd.read_csv(r"E:\Placement_Prediction_System\Test.csv")
        for i in range(1,len(abc)):
            check = abc.iloc[i:i+1]
            sub1 = check['10th'][i]
            sub2 = check['12th'][i]
            sub3 = check['1st_year'][i]
            sub4 = check['2nd_year'][i]
            sub5 = check['3rd_year'][i]
            total = [sub1,sub2,sub3,sub4,sub5]
            avg = sum(total)/len(total)
            
            if avg>50:
                mail = check['Mail'][i]
                print(mail)
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from email.mime.base import MIMEBase
                from email import encoders
                
                fromaddr = 'projectandroidengg@gmail.com'
                toaddr = str(mail)
            
                msg = MIMEMultipart()
            
                msg['From'] = fromaddr
            
                msg['To'] = toaddr
            
                password = '9689544204'
            
            
                msg['Subject'] = "Placement Update"
            
            
                body = "You are eligible for drive for company {} on {}".format( company_value,date_value)
        
            
            
                msg.attach(MIMEText(body, 'plain'))
            
            
                #filename = f
                
                s = smtplib.SMTP('smtp.gmail.com', 587)
            
            
                s.starttls()
            
                try:
                    s.login(fromaddr,password)
            
            
                    text = msg.as_string()
            
            
                    s.sendmail(fromaddr, toaddr, text)
            
                    Success = tk.Label(root, text="Mail Sent \nSuccessfully !", width=15, height=2, background="white", foreground="black",
                                     font=("Tempus Sans ITC", 15, "bold"))
                    Success.place(x=10, y=500)
                    print("Mail Sent Suucessfully !")
            
                except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
                    Success = tk.Label(root, text="Oops ! \nMail Not Sent !", width=15, height=2, background="white",
                                    foreground="black",
                                    font=("Tempus Sans ITC", 15, "bold"))
                    Success.place(x=10, y=500)
                    print("Oops Mail Not Sent !")

                
    submit = tk.Button(new_entry,text='Submit',command =into ,font=('Times New Roman',10),width=14,bg='green',fg='white')
    submit.place(x=5,y=90)
    new_entry.mainloop()


"""
abc = pd.read_csv(r"E:\Placement_Prediction_System\Test.csv")

abc1 = abc[abc['Name']=='BABAR AJAY DEEPAK']
abc1['Mail'][0]
"""
def EXIT():
    root.destroy()



# button1 = tk.Button(root,text="Decision Tree",command=DT,font=('Times New Roman',12,'italic'),width=15,bg='black',fg='linen')
# button1.place(x=50,y=100)

# button2 = tk.Button(root,text="Naivey Bayes",command=NB,font=('Times New Roman',12,'italic'),width=15,bg='black',fg='linen')
# button2.place(x=50,y=200)

# button3 = tk.Button(root,text="K-Nearest Neighbor",command=KNN,font=('Times New Roman',12,'italic'),width=15,bg='black',fg='linen')
# button3.place(x=50,y=300)

button4 = tk.Button(root,text="Train Model",command=SVM,font=('Times New Roman',12,'italic'),width=15,bg='black',fg='linen')
button4.place(x=50,y=100)

button6 = tk.Button(root,text="New COM",command=NEW_COM,font=('Times New Roman',12,'italic'),width=15,bg='black',fg='linen')
button6.place(x=50,y=600)

button7 = tk.Button(root,text="EXIT",command=EXIT,font=('Times New Roman',12,'italic'),width=15,bg='red',fg='linen')
button7.place(x=300,y=600)

root.mainloop()


