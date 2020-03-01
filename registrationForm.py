#For creation database of student
import cv2
from time import sleep

#no of image of one person in database
noOfImage = 1000
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)
while True:
        #Break after taking 100 img
        if noOfImage == 1000:
            name = input("Enter name")
        noOfImage = noOfImage - 1
        if noOfImage == 0:
            break
        
        #Capture frame by frame
        check, frame = webcam.read()
        
        #put no. on image
        textOnImage = "Image left to take {0}".format(noOfImage)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)
        fontScale = 1
        color = (225,0,0)
        thickness = 1 
        cv2.putText(frame,
                    textOnImage,
                    org,font,fontScale,color,thickness)
        
        #show the current img
        cv2.imshow("image", frame)
        key = cv2.waitKey(1)

        #conver to gray
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)



   

