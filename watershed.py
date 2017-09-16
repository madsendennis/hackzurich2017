# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt
#imgRaw = cv2.imread('images/water_coins.jpg', cv2.IMREAD_COLOR)
imgRaw = cv2.imread('raw/normal3.jpg', cv2.IMREAD_COLOR)
b,g,r = cv2.split(imgRaw)
gray = cv2.cvtColor(imgRaw, cv2.COLOR_BGR2GRAY)

img = gray
print(img.shape)

#hist,bins = np.histogram(img.flatten(),256,[0,256])
#cdf = hist.cumsum()
#cdf_normalized = cdf * hist.max()/ cdf.max()

thresholdLevel= cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU
print("Threshold: ", thresholdLevel)
ret, thresh = cv2.threshold(img,0,255,thresholdLevel)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(thresh, cmap = 'gray')
plt.show()

# noise removal
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
plt.subplot(121),plt.imshow(sure_bg, cmap = 'gray')
plt.subplot(122),plt.imshow(sure_fg, cmap = 'gray')
plt.show()


# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

plt.subplot(111),plt.imshow(markers)
plt.show()

markers = cv2.watershed(imgRaw,markers)
imgRaw[markers == -1] = [255,0,0]

plt.subplot(111),plt.imshow(imgRaw)
plt.show()

print("Number of grains: ", ret)
