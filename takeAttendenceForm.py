#Input image form file explorer to detect
from tkinter import filedialog
from tkinter import *
import cv2

root = Tk()
#It create file explorer to take img dir.
root.filename = filedialog.askopenfilename(
    initialdir = "/",
    title = "Select file",
    filetypes = (("jpeg files","*.jpg"),("all file","*.*"))
    )
    
print(root.filename)
img = cv2.imread(root.filename)
cv2.imshow("img",img)

