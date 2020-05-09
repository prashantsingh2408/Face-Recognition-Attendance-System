#Incomplete
# Match face, detect name and save attendence.
import cv2
import os
from time import sleep

#Take image
webcam = cv2.VideoCapture(0)
check, frame = webcam.read()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = detector.detectMultiScale(gray,1.1,5)


cv2.imshow("image", frame)
key = cv2.waitKey(1)