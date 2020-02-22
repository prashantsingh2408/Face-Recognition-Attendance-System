import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#import image
img = cv2.imread('test.jpg')

#converting to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detectin face
#1.1  scalefactor
#5   minneighbour
faces = face_cascade.detectMultiScale(gray, 1.1, 6)

# Creating rectangle 
for (x, y ,w, h) in faces:#face is list of 4-element list
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
cv2.imshow('img', img)
cv2.waitkey()

