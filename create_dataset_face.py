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
    cv2.imwrite(current_path + "/face_database/" + name +"/" + str(np.random.randint(1000)) + ".png",crop_img)

#----Function to return all JPEG file's path in a directory
def getFiles(path):
    folder = os.fsencode(path)
    filenames = []
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.JPG')):
            filenames.append(path + '\\' + str(filename))
    return filenames


#----Variables----
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

current_path = os.getcwd()

counter = 0
counter1 = 0

#-------Creating list of training filenames of known faces along with path----
known_faces = getFiles('')
known_faces_encoded = knownFacesCollecting(known_faces)


#-------Creating list of training filenames along with path-----
farewell_images = getFiles('F:\Pictures\BE Photoshoot')

#-------Processing Farewell Images--------------
for path in farewell_images:
    image = face_recognition.load_image(path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encoding(image,face_locations)
    




