from tkinter import *
from tkinter import ttk
from openpyxl import *


#read xl on sheet object
wb = load_workbook('record.xlsx')

#sheet object
sheet = wb.active 

window = Tk()
window.title("Resistration Form")
window.geometry('400x400')
window.configure(background = "grey");

a = Label(window ,text = "Name",width=22).grid(row = 0,column = 0)
b = Label(window ,text = "Course",width=22).grid(row = 1,column = 0)
c = Label(window,text="Stream",width=22).grid(row = 2, column = 0)
d = Label(window ,text = "Email Id",width=22).grid(row = 3,column = 0)
e = Label(window ,text = "Contact Number",width=22).grid(row = 4,column = 0)

a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
e1 = Entry(window).grid(row = 4,column = 1)

def show():
    print("Thank you for submitting your response")

def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)

btn = ttk.Button(window ,text="Submit",command=show).grid(row=5,column=0)
window.mainloop()
