import cv2

#image import
path  = r"C:\Users\prashant\Documents\prog\face-recognition-attendence-system\data\Prashant\prashant2.jpg"
img = cv2.imread(path)
cv2.imshow("image",img)

#converting to gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect face
path_cas = cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(path_cas)
faces = face_cascade.detectMultiScale(
        imgGray,
        scaleFactor = 1/20,
        minNeighbors = 3,
        minSize = (30,30)
)

#Create rectangle
for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h),(225, 0, 0), 3)

cv2.imshow('img', img)
cv2.waitkey()

