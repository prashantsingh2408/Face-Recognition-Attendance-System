import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    #Capture frame by frame
    ret, frame = cap.read()
    
    #operation on frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #display the resulting frame
    cv2.imshow('Frame',gray)

    if cv2.waitKey(1) &
