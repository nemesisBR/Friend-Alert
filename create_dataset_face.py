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
    cv2.imwrite("F:\Pictures\Delhi 2015\Photoshop\\" + name + str(np.random.randint(1000)) + ".png",crop_img)
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


#----Variables----

face_names = []
frame_number = 0

current_path = os.getcwd()

counter = 0
counter1 = 0

#-------Creating list of training filenames of known faces along with path----
known_faces , face_names = getFiles('F:\GitHub\Friend Alert\KnownImages')
known_faces_encoded = knownFacesCollecting(known_faces)
 


#-------Creating list of training filenames along with path-----
farewell_images ,file_names = getFiles('F:\Pictures\BE Photoshoot')

#-------Processing Farewell Images--------------
count = 0
for path in farewell_images:
    count = count + 1
    print(count)
    faceNamesPhoto = []
    face_locations = []
    face_encodings = []
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image,face_locations)
    
    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(known_faces_encoded,face_encoding, tolerance = 0.50)
        
        name = getName(match, face_names)
        faceNamesPhoto.append(name)
    
    for (top, right, bottom, left), name in zip(face_locations, faceNamesPhoto):
        if not name:
            continue
        crop_image = image[top:bottom, left:right]
        storeImages(name, crop_image)


