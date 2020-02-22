import cv2
#.CascadeClassifier:'harrcasca....' contain def of face
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#import image
img = cv2.imread('test.jpg')

#converting to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#.detectMultiScale(image,scalefactor,minneighbour)
#return: list of 4-element list.
#each list represent a image coordinates.
#[[x,y,width,height],[....],...]
faces = face_cascade.detectMultiScale(gray, 1.1, 6)

#.rectangle(img,coord1,coord2,RBG,thickness)
for (x, y ,w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
cv2.imshow('img', img)
cv2.waitkey()

