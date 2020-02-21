import numpy as np
import os

def collect_dataset():
    '''
    Purpose:Take image from the storage.
    '''
    images = [] 
    labes = [] #for inds exing every image
    labels_dic = []

    #List of person folder([Prashant,Alok] in this case)
    people = [person for person in os.listdir('data/')]
    
    #Iterate over every person folder(Prashant,Alok)
    #Prashant folder contain image in .jpg
    for i,person in enumerate(people):
        labels_dic[i] = person
        #Iterate over image present in (Prashant,Alok)
        for image in os.listdir('data/' + person):
            if image.endwith('.jpg'):
                images.append(cv2.imread('data/' + person + '/' + image,0))
                labes.append(i)
    #images:Contain all images
    # labes:0 for person Prashant, 1 for alok can so on.
    # labels_dict:{0:'prashant',1:'alok'} is this case.            
    return(images, np.array(labes), labels_dict)
image, labels, labes_dic = collect_dataset()


