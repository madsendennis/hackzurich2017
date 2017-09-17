# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 04:46:13 2017

An example on how to get the evaluation of an image

@author: djordje
"""
import cv2, os, sys
import numpy as np

scriptpath  = 'predict.py'
sys.path.append(os.path.abspath(scriptpath))
import predict

not_safe_image = cv2.imread("data_set/not_safe/45-1.png", cv2.IMREAD_GRAYSCALE)

not_safe_image_array = []
for row in not_safe_image:
    not_safe_image_array = np.concatenate((not_safe_image_array, row))

chk = Check(not_safe_image_array)
print(chk.Label())

safe_image = cv2.imread("data_set/safe/1.png", cv2.IMREAD_GRAYSCALE)
safe_image_array = []
for row in safe_image:
    safe_image_array = np.concatenate((safe_image_array, row))

chk = Check(safe_image_array)
print(chk.Label())