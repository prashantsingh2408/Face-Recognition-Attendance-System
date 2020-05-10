#Completed
#For creation database of student, save in /img directory.
import cv2
from time import sleep
import os # for folder access

MAXSAMPLE = 100 # no of img to be taken of one person.

noOfImage = MAXSAMPLE
webcam = cv2.VideoCapture(0) # open camera
mainDir = os.getcwd() # get current director of this file

sleep(2) # give time to person to adject face.

#start taking image
while True:
        #at staing input name of person 
        if noOfImage == MAXSAMPLE:
            #Input name
            name = input("Enter name to register\n")
            #Change dir to 'imgDataBase' where image store
            os.chdir("img")
            #Create a directory(folder) with person name
            os.mkdir(name)
            #Return to main dir
            os.chdir(mainDir)
         
        check, frame = webcam.read()
        #Capture frame by frame
        # .read() -> return [status,image frame]
        # status  -> True if image taken otherwise False
        
        #Detect face
            #converty to gray for good detection
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #detect face
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = detector.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=5)
        
  
        #(x,y,w,h) -> axis, width and height of face
        for (x,y,w,h) in faces:
            
            #create rec
            color = (255, 0 , 0) #color of recangle
            thickness = 2 # thickness of rectangle
            cv2.rectangle(frame,(x,y),(x+w,y+h),color ,thickness)
            
            #display image
            #put no.(text) on image
            textOnImage = "Image left to take {0}".format(noOfImage)
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50) #position form ORiGin
            fontScale = 1 #size of text
            color = (0,0,255) #optional
            thickness = 1 #optional
            cv2.putText(frame,
                        textOnImage,
                        org,font,fontScale,color,thickness)

            #show the current img
            cv2.imshow("image", frame)
            key = cv2.waitKey(1) #wait, otherwise system hacks and stop.

            #save Face
            crop_face = frame[y:y+h, x:x+w]
            
            #change dir
            os.chdir("img")
            os.chdir(name)
            
            #write img
            imgName = "{0}{1}.jpg".format(name,noOfImage)# name of image
            cv2.imwrite(imgName,crop_face)
            
            #Return to main dir
            os.chdir(mainDir)
        
        #Break when all image are taken
        noOfImage = noOfImage - 1
        if noOfImage == 0:
            break



        

   

