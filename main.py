import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from datetime import datetime


def readImage(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR) #IMREAD_GRAYSCALE IMREAD_UNCHANGED IMREAD_COLOR
    b,g,r = cv2.split(img)
    th, bw = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return img, bw

def denoiseImage(img):
    # noise removal
    kernel = np.ones((13,13),np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel, iterations = 2)
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)
    # Marker labelling
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    labels = labels+1
    # Now, mark the region of unknown with zero
    labels[unknown==255] = 0
    return labels, sure_bg, sure_fg

def main(imgPath):
    imgRaw, equ = readImage(imgPath)
    imgRawOrig = imgRaw.copy()

    



if __name__ == "__main__":
    main('dorde/black_contaminated_1.jpg')
