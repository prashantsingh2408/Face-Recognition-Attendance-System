#completed
import os
import cv2
from PIL import Image
import numpy as np
import pickle

print("traning start...")

#Load dir of images for training
base_dir = os.path.dirname(os.path.abspath(__file__))
#.abspath(__file__) gives path of current file wich is ...face-re.../trainner.py
#.dirname gives ...face-re/ as it remove trainner.py form path

img_dir1 = os.path.join(base_dir, "img")
#join the base dir with img to get dir of ...face-re.../img/ 

#DISABLEimg_dir2 = os.path.join(base_dir, "imgOtherSrc")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Create recognizer 
recognizer = cv2.face.LBPHFaceRecognizer_create()
#We need to train this recognizer

current_id = 0
label_ids = {} #{'name', id}
labels = [] #id of person 
train = []	#contain image to be train

for root, dirs, files in os.walk(img_dir1):
	#print(root)
	#print(files)
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
			label = os.path.basename(root).replace(" ", "-").lower()
			#label can be name of person folder like 'prashant', 'alok' where image store
			#print('label',label)
			#.repalce -> in the case label is like prashant singh it conver it to
			#prashant-singh to reduce error in some system

			#provie each each lable a id
			#it is require at the time of training
			if not label in label_ids:#label name should not more then one time in label_ids{}
				label_ids[label] = current_id
				current_id += 1
			id = label_ids[label]

			pil_img = Image.open(path).convert("L")#L for grayscale
			#DISABLEsize = (550,550)#no need to resize
			final_img = pil_img #DISpil_img.resize(size, Image.ANTIALIAS)#resize
			img_array = np.array(final_img,"uint8")
			faces = face_cascade.detectMultiScale(img_array, scaleFactor = 1.1, minNeighbors=5)
			cv2.waitKey(1)
			for (x,y,w,h) in faces:
				roi = img_array[y:y+h, x:x+w] # roi = region of interest (face of person in img)
				
				train.append(roi)#it contain all image face
				labels.append(id)#it contain labels corresponding to faces in train[]

#label will use in recognizer.py modules,so save in file
with open("labels.pickle",'wb') as f:
	pickle.dump(label_ids,f)

try:#if no image is present in exception arise.

	recognizer.train(train,np.array(labels))
	#recognizer needs train[] and name(labels[]) of ther person to train

	recognizer.save('tranner.yml')
	print("trained")
	
except:
	print("no iamge to recognize, please upload image")
	print("untrained")

