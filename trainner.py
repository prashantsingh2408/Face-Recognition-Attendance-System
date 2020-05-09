#Incomplete
import os
import cv2
from PIL import Image
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir, "img")


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
labesls = [] # store name of persons
train = []	

for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
			label = os.path.basename(root).replace(" ", "-").lower()
			#print(label)
			#print(path)

			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id = label_ids[label]
			print(label_ids[label])
			pil_img = Image.open(path).convert("L")#grayscale
			size = (550,550)
			final_img = pil_img.resize(size, Image.ANTIALIAS)
			img_array = np.array(final_img,"uint8")
			print(img_array)
			faces = face_cascade.detectMultiScale(img_array, scaleFactor = 1.5, minNeighbors=5)
			
			for (x,y,w,h) in faces:
				roi = img_array[y:y+h, x:x+w] # roi = region of interest (face of person in img)
				train.append(roi)
				label.append(id)

print(train)
print()
