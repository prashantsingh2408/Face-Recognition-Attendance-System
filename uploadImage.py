#For creation database of student, save in /img directory.
import cv2
from time import sleep
import os # for folder access

MAXSAMPLE = 300 # no of img to be taken of one person.

sleep(2) # give time to person to adject face.

#take many image using loop
while (MAXSAMPLE > 0):
        #at staing input name of person 
        if MAXSAMPLE == 300
            #Input name, rollNo and claaStu
            name = input("Enter name to register\n")
            rollNo= input("Enter roll no\n")
            classStu = input("Enter year(1,2,3,4)\n")

            #Change dir to 'img' where image store
            os.chdir("img")

            #Create a directory(folder) with person name and move in it
            try:
                os.mkdir(name+ ' ' + rollNo + ' ' + classStu)
                os.chdir(name+ ' ' + rollNo + ' ' + classStu)
            except:
                print('your photo exit,adding more')
            
            # initialize camera
            webcam = cv2.VideoCapture(0)

            #Decrement MAXSAMPLE by 1
            MAXSAMPLE = MAXSAMPLE - 1  

        #Take image
        check, frame = webcam.read()
        # .read() -> return [status,image frame]
        # status  -> True if image taken otherwise False
        
        #converty to gray for good detection
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #detect face
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = detector.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=5)
        
        for (x,y,w,h) in faces: 
        #(x,y,w,h) -> axis, width and height of face
            # create rectangle
            color = (255, 0 , 0) #color of recangle
            thickness = 2 # thickness of rectangle
            cv2.rectangle(frame,(x,y),(x+w,y+h),color ,thickness)
            
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

            #Diplay current img
            cv2.imshow("image", frame)
            key = cv2.waitKey(1) #wait, otherwise system hacks and stop.

            #save Face
            crop_face = frame[y:y+h, x:x+w]
            imgName = "{0}{1}.jpg".format(name,MAXSAMPLE)
            cv2.imwrite(imgName,crop_face)
                   
        #For breaking loop when all image are taken
        MAXSAMPLE = MAXSAMPLE - 1



        

   

