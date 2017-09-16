import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from datetime import *

filename = 'stuff.jpg'
img = cv2.imread(filename,0)
#img = cv2.medianBlur(img,5)
img = cv2.GaussianBlur(img,(5,5),0)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(0, 4):
    plt.subplot(2, 2, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

image, contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
cnt = contours[0]
cv2.drawContours(image, [cnt],-1,(0,0,0),1)
#plt.plot(image)
#plt.show()
#cv2.imshow('contours', image)   
cv2.imwrite(filename + '-contours.png',image)

#cv2.waitKey(0) ## Wait for keystroke
#cv2.destroyAllWindows() ## Destroy all windows

# Directory for storing grain contures
newpath = "C:/Users/djord/OneDrive/Shljaka/HackZurich2017/test/contures/" +  datetime.today().strftime("%d-%b-%Y %Hh%Mm%S")
if not os.path.exists(newpath):
    os.makedirs(newpath)

### Extracting contours
for i in range(0, len(contours)):
    if (i % 2 == 0):
       cnt = contours[i]
       #mask = np.zeros(im2.shape,np.uint8)
       #cv2.drawContours(mask,[cnt],0,255,-1)
       x,y,w,h = cv2.boundingRect(cnt)
       #cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 1)
       # cv2.imshow('Features', image)
       cv2.imwrite(newpath + '/' + str(i) +'.png', image[y:y+h,x:x+w])

cv2.destroyAllWindows()
