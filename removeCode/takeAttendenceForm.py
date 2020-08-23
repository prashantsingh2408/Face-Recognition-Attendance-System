#Input image form file explorer to detect
from tkinter import filedialog
from tkinter import *
import cv2
import time

root = Tk()
#It create file explorer to take img dir.
root.filename = filedialog.askopenfilename(
    initialdir = "/",
    title = "Select file",
    filetypes = (("jpeg files","*.jpg"),("all file","*.*"))
    
    )
img = cv2.imread(root.filename)#Run time error,debug require
cv2.imshow("img",img)#Run time error,debug require
time.sleep(3)

