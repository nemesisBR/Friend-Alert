# -*- coding: utf-8 -*-
#----------------------------------------------
#--- Author         : Ahmet Ozlu
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 21st September 2017
#----------------------------------------------


#----Modified by-------------------------------
#--- Author         : Boby Robert
#--- Mail           : robert.boby95@gmail.com
#---------------------------------------------- 

import face_recognition
import cv2
import os
import numpy as np
import multiprocessing as mp
import time



#---------Function to Load Known Images-------
def knownFacesCollecting(filenames):
    known_faces = []
    for path in filenames:
        image = face_recognition.load_image_file(path)
        image_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(image_encoding)
    return known_faces

#----Function to store images 
def storeImages(name, crop_img):
    #print("F:\Pictures\Delhi 2015\Photoshop\\" + name + str(np.random.randint(1000)) + ".png")
    print("Saved:", name)
    cv2.imwrite("F:\GitHub\Friend Alert\Dataset\\" + name +"\\"+ str(np.random.randint(1000)) + ".jpg",crop_img)
    #print(current_path + "F:\Pictures\Delhi 2015\Photoshop\\" + name + str(np.random.randint(1000)) + ".png")
#----Function to return all JPEG file's path in a directory
def getFiles(path):
    folder = os.fsencode(path)
    filenames = []
    names = []
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.JPG')):
            filenames.append(path + '\\' + str(filename))
            names.append(str(filename[0:-4]))
    return filenames, names

#----Function to get name of matched face---------
def getName(match,known_face_names):
    for i in range(27):
        if match[i]:
            return known_face_names[i]
        else:
            continue
#-----Function to process & store images-----------
def identify_faces(farewell_images,known_faces_encoded,known_face_names):
    count = 0
    #face_names = []
    for path in farewell_images:
        count = count + 1
        print(count)
        faceNamesPhoto = []
        face_locations = []
        face_encodings = []
        image = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image,face_locations)
'''    
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(known_faces_encoded,face_encoding, tolerance = 0.50)
            name = 'x'
            #name = getName(match, known_face_names)
            faceNamesPhoto.append(name)
            
        for (top, right, bottom, left), name in zip(face_locations, faceNamesPhoto):
            if not name:
                continue
            crop_image = image[top:bottom, left:right]
            storeImages(name, crop_image)
        time.sleep(1)
'''

#-------Creating list of training filenames of known faces along with path----
known_faces , known_face_names = getFiles('F:\GitHub\Friend Alert\KnownImages')
known_faces_encoded = knownFacesCollecting(known_faces)

#--------Create folders for each known images----------
#for name in known_face_names:
#    os.mkdir("F:\GitHub\Friend Alert\Dataset\\" + name)
 


#-------Creating list of training filenames along with path-----
farewell_images,file_names = getFiles('F:\Pictures\BE Photoshoot')

f1 = farewell_images[0:10]
f2 = farewell_images[10:20]
#-------Processing Farewell Images--------------
if __name__ == "__main__":
    p1 = mp.Process(target = identify_faces, args = (f1,known_faces_encoded,known_face_names))
    #p2 = mp.Process(target = identify_faces, args = (f2,known_faces_encoded,known_face_names, ))
    
    p1.start()
    #p2.start()
    
    p1.join()
    #p2.join()
    
    print("finished")
#identify_faces(farewell_images,known_faces_encoded,known_face_names)


