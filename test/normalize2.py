from os import listdir
from os.path import isfile, join
import numpy as np
import cv2

###################
# Normalization is done by discarding too small or too big images
# and by fiiling in for the missing rows by adding rows/columns with 0s until
# the size of the image is 100x100
# Moreover, the that are bigger than 200px in some dimension are split to two
# smaller ones and added separately
###################

# limits for image size
max_height = 100
min_height = 50
max_width = 100
min_width = 50

def split(img):
    height, width= img.shape
    if (width > height):
        img1 = img[:max_height, :max_width]
        img2 = img[:max_height, max_width:2*max_width]
        return img1, img2
        
    if (width < height):
        img1 = img[:max_height, :max_width]
        img2 = img[max_height:2*max_height, :max_width]
        return img1, img2
        
    
def fill_the_missing(img):
    height, width = img.shape

    # Filling rows
    if (height < max_height):
        tmp = np.array([np.zeros(width)])
        while (height < max_height):
            img = np.concatenate((img, tmp))
            height += 1
            
    height, width = img.shape
    # Filling columns
    if (width < max_width):
        tmp = np.zeros(height)
        while (width < max_width):
            img = np.c_[img, tmp]
            width += 1

    return img

# List all the grains from the 'okay' folder
path = 'okay/'
data_set_path_safe = "data_set/safe/"

images_safe = [f for f in listdir(path) if isfile(join(path, f))]

# Filter the images based on the size 
#   - if one of the dimensions is > 100 px     - discard
#   - if the image has both dimentions < 50 px - discarded    
counter = 0     
for image_path in images_safe:
    img = cv2.imread(path + image_path, cv2.IMREAD_GRAYSCALE)
    height, width= img.shape
    
    if (width < min_width and height < min_height):
        continue

#    # We don't do the splitting in the case of the 'okay' datasets
#    # In case the image has one of the dimensions twice the size of the allowed
#    # we split it into two images
#    if (width > 2*max_width or height > 2*max_height):
#        img1, img2 = split(img)
#        counter += 2
#        cv2.imwrite(data_set_path_safe + image_path + "1", fill_the_missing(img1))
#        cv2.imwrite(data_set_path_safe + image_path + "2", fill_the_missing(img2))
#        continue

    if (width > max_width or height > max_height):
        continue
        
        
    # Save the resized image to the new folder
    counter += 1
    cv2.imwrite(data_set_path_safe + image_path, fill_the_missing(img))
    
print("Out of " + str(len(images_safe)) + " images " + str(counter) + " passed the filter in the 'okay' folder.")


# List all the grains from the 'okay' folder
path = 'contaminated/'
data_set_path_safe = "data_set/not_safe/"

images_not_safe = [f for f in listdir(path) if isfile(join(path, f))]

# Filter the images based on the size 
#   - if one of the dimensions is > 100 px     - discard
#   - if the image has both dimentions < 50 px - discarded         
counter = 0    
for image_path in images_not_safe:
    img = cv2.imread(path + image_path, cv2.IMREAD_GRAYSCALE)
    height, width= img.shape
    
    if (width < min_width and height < min_height):
        continue

    # In case the image has one of the dimensions twice the size of the allowed
    # we split it into two images
    if (width > max_width+min_width or height > max_height+min_height):
        img1, img2 = split(img)
        counter += 2
        cv2.imwrite(data_set_path_safe + image_path[:image_path.find('.')] + "-1" + image_path[image_path.find('.'):], fill_the_missing(img1))
        cv2.imwrite(data_set_path_safe + image_path[:image_path.find('.')] + "-2" + image_path[image_path.find('.'):], fill_the_missing(img2))
        continue
    
    if (width > max_width or height > max_height):
        continue
    
    # Save the resized image to the new folder
    counter += 1
    cv2.imwrite(data_set_path_safe + image_path, fill_the_missing(img))
    
print("Out of " + str(len(images_not_safe)) + " images " + str(counter) + " passed the filter in the 'contaminated' folder.")
    

