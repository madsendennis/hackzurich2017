# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 02:09:28 2017

@author: brlauuu
"""

from os import listdir
from os.path import isfile, join
import numpy as np
import cv2
from random import shuffle

def toArrayOfArrays(image):
    result = []
    for row in image:
        result = np.concatenate((result, row))
        
    return result
    
def array2string(array):
    result = ""
    for a in array:
        result += str(a) + ","

    return result[:-1] + "\n"

data_set_path_safe = "data_set/safe/"
data_set_path_not_safe = "data_set/not_safe/"

images_safe     = [data_set_path_safe + f     for f in listdir(data_set_path_safe)     if isfile(join(data_set_path_safe, f))]
images_not_safe = [data_set_path_not_safe + f for f in listdir(data_set_path_not_safe) if isfile(join(data_set_path_not_safe, f))]

               
data = []
for image in images_safe:
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    data.append(np.concatenate(([1], toArrayOfArrays(img))))

for image in images_not_safe:
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    data.append(np.concatenate(([0], toArrayOfArrays(img))))

shuffle(data)
header = ["label"]
for i in range(0,10000):
    header.append('c'+str(i))

with open('data.csv', 'w') as file:
    file.write(array2string(header))
    for d in data:
        file.write(array2string(d))

    