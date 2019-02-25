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


#---------Function to Load Known Images-------
def knownFacesCollecting(path):
    known_faces = []
    #T0DO---Loop over every known images---
    image = face_recognition.load_image_file('''FILEname''')
    image_encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(image_encoding)
    #----------------
    return known_faces

#----Function to store images 
def storeImages(name, crop_img):
    cv2.imwrite(current_path + "/face_database/" + name +"/" + str(np.random.randint(1000)) + ".png",crop_img)

#----Variables----
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

current_path = os.getcwd()

counter = 0
counter1 = 0


