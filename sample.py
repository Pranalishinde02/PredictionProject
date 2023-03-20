import tkinter
from PIL import ImageTk, Image
import os
  
# creating main window
root = tkinter.Tk()
root.geometry("700x500")
# loading the image
img = ImageTk.PhotoImage(Image.open("not_ele.png"))
  
# reading the image
panel = tkinter.Label(root, image = img)
  
# setting the application
panel.place(x=0,y=0)
  
# running the application
root.mainloop()