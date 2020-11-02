#completed
import os
import cv2
from PIL import Image
import numpy as np
import pickle

print("traning start...")

#Load dir of images for training
#base_dir = os.path.dirname(os.path.abspath(__file__))
#.abspath(__file__) gives path of current file which is ...face-re.../trainner.py
#.dirname gives ...face-re/ as it remove trainner.py form path

#img_dir1 = os.path.join(base_dir, "img")
#join the base dir with img to get dir of ...face-re.../img/ 

#Use for Detecting face later
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

os.chdir("img")
#DISABLEimg_dir2 = os.path.join(base_dir, "imgOtherSrc")


#Create recognizer 
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer = cv2.face_LBPHFaceRecognizer_create()
#We need to train this recognizer
#recognizer needs train[] and name(labels[]) of ther person to train

current_id = 0
labels_ids = {} #{'name', id}
ids = [] #id of person 
faces = []	#contain image to be train


for root, dirs, files in os.walk(os.getcwd()):
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
			if not label in labels_ids:#label name should not more then one time in label_ids{}
				labels_ids[label] = current_id
				current_id += 1

			img = Image.open(path).convert("L")#L for grayscale
			#DISABLEsize = (550,550)#no need to resize
			#final_img = pil_img #DISpil_img.resize(size, Image.ANTIALIAS)#resize
			img_array = np.array(img,"uint8")
			face = detector.detectMultiScale(img_array, scaleFactor = 1.1, minNeighbors=5)
			cv2.waitKey(1)
			for (x,y,w,h) in face:
				roi = img_array[y:y+h, x:x+w] # roi = region of interest (face of person in img)
				
				faces.append(roi)#it contain all image face
				ids.append(labels_ids[label])#it contain labels corresponding to faces in train[]

#label will use in recognizer.py modules,so save in file
os.chdir('..')
labelsFile = open("labels.pickle",'wb')
pickle.dump(labels_ids,labelsFile)


try:#if no image is present in exception arise.

	recognizer.train(faces,np.array(ids))
	#recognizer needs train[] and name(labels[]) of ther person to train

	recognizer.save('tranner.yml')
	print("trained")
	
except:
	print("no image to recognize, please upload image")
	print("untrained")

