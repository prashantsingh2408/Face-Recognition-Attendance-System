#Completed
#For creation database of student, save in /img directory.
import cv2
from time import sleep
import os # for folder access
MAXSAMPLE = 200

#no of image of one person in database
noOfImage = MAXSAMPLE
webcam = cv2.VideoCapture(0)
mainDir = os.getcwd()
# give time to person to adject face.
sleep(2)

#start taking image
while True:
        #at staing 
        if noOfImage == MAXSAMPLE:
            #Input name
            name = input("Enter name")
            #Change dir to 'imgDataBase' where image store
            os.chdir("img")
            #Create a directory(folder) with person name
            os.mkdir(name)
            #Return to main dir
            os.chdir(mainDir)
        
        #Break while loop after taking 100 img
        noOfImage = noOfImage - 1
        if noOfImage == 0:
            break
        
        #Capture frame by frame
        # .read() -> return [status,image(frame)]
        # status  -> True if image taken otherwise False 
        check, frame = webcam.read()
        
        #Detect face
            #converty to gray for good detection
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #detect face
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = detector.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=5)
        
        #rectangle create and save img
        for (x,y,w,h) in faces:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
            crop_face = gray[y:y+h, x:x+w]
            #change dir
            os.chdir("img")
            os.chdir(name)
            #write img
            imgName = "{0}{1}.jpg".format(name,noOfImage)
            cv2.imwrite(imgName,crop_face)
            #Return to main dir
            os.chdir(mainDir)
            #update frame
        frame = gray

        #put no.(text) on image
        textOnImage = "Image left to take {0}".format(noOfImage)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #position form ORiGin
        org = (50, 50)
        #size of text
        fontScale = 1
        color = (0,0,255)#optional
        thickness = 1#optional
        cv2.putText(frame,
                    textOnImage,
                    org,font,fontScale,color,thickness)

        #show the current img
        cv2.imshow("image", frame)
        key = cv2.waitKey(1)

        

   

