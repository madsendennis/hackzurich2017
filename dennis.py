# -*- coding: utf-8 -*-


import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from datetime import datetime

print("Stuff")

imgRaw = cv2.imread('dorde/black_contaminated_1.jpg', cv2.IMREAD_COLOR) #IMREAD_GRAYSCALE IMREAD_UNCHANGED IMREAD_COLOR
imgRawOrig = imgRaw.copy()
img_b,img_g,img_r = cv2.split(imgRaw)
img_gray = cv2.cvtColor(imgRaw, cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(img_r)


#equ_th, dst = cv2.threshold(equ, 0, 200, cv2.THRESH_BINARY);

th, bw = cv2.threshold(img_r, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
edges = cv2.Canny(imgRaw, th/2, th)

plt.subplot(3,3,1),plt.imshow(imgRaw)
plt.subplot(3,3,2),plt.imshow(bw, 'gray')

# noise removal
kernel = np.ones((13,13),np.uint8)
opening = cv2.morphologyEx(bw, cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

plt.subplot(3,3,4), plt.imshow(sure_bg)
plt.subplot(3,3,5), plt.imshow(sure_fg)

# Marker labelling
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
labels = labels+1
# Now, mark the region of unknown with zero
labels[unknown==255] = 0


labels = cv2.watershed(imgRaw, labels)
imgRaw[labels == -1] = [255,0,0]

plt.subplot(3,3,3),plt.imshow(labels)
plt.subplot(3,3,6),plt.imshow(imgRaw)


print("Number of markers: ", num_labels)

newpath = "test/contures/" +  datetime.today().strftime("%d-%b-%Y_%Hh%Mm%S")
if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in range(1, num_labels):
    if False: #i < 50:    
        newLabel = labels.copy()
        newLabel[newLabel != i] = 0
        newLabel[newLabel == i] = 255
        newLabel = newLabel.astype(np.uint8)
        th, imgloc = cv2.threshold(newLabel, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        image, contours, hierarchy = cv2.findContours(imgloc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        for cont in contours:
            x,y,w,h = cv2.boundingRect(cont)
            cv2.imwrite(newpath + '/' + str(i) +'.png', imgRawOrig[y:y+h,x:x+w])


numNotBG = np.count_nonzero(bw.flatten())
print("Not Background: ", numNotBG)
labelCp = labels.copy()
labelCp[labelCp < 2] = 0
numOK = np.count_nonzero(labelCp.flatten())
print("Good stuff: ", numOK)
percOk = (numOK/numNotBG)*100.0
print("OK: ", percOk)



fred = np.fft.fft2(img_r)
fshiftred = np.fft.fftshift(fred)
magnitude_spectrum_red = 20*np.log(np.abs(fshiftred))
plt.subplot(3,3,7),plt.imshow(magnitude_spectrum_red, 'gray')


# Overlay image
total = bw
good = labels.copy()

alpha = 0.5
overlay = imgRawOrig.copy()
output = imgRawOrig.copy()

output[total > 0] = (255, 0, 0)
output[labels > 1] = (0, 255, 0)

cv2.addWeighted(overlay, alpha, output, 1 - alpha, 	0, output)


plt.subplot(3,3,8),plt.imshow(output)


plt.show()

cv2.imshow('precision', output)
