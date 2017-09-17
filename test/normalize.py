from os import listdir
from os.path import isfile, join
import cv2

###################
# Normalization is done by discarding too small or too big images
# and by resizing (streaching) the images to 100x100
###################

# limits for image size
max_height = 100
min_height = 50
max_width = 100
min_width = 50

# List all the grains from the 'okay' folder
path = 'okay/'
data_set_path_safe = "data_set/safe/"

images_safe = [f for f in listdir(path) if isfile(join(path, f))]

# Filter the images based on the size 
#   - if one of the dimensions is > 100 px     - discard
#   - if the image has both dimensions < 50 px - discarded    
counter = 0     
for image_path in images_safe:
    img = cv2.imread(path + image_path, cv2.IMREAD_GRAYSCALE)
    height, width= img.shape
    
    if (width > max_width or height > max_height):
        continue

    if (width < min_width and height < min_height):
        continue
    
    # Save the resized image to the new folder
    counter += 1
    cv2.imwrite(data_set_path_safe + image_path, cv2.resize(img, (100, 100)))
    
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
    
    if (width > max_width or height > max_height):
        continue

    if (width < min_width and height < min_height):
        continue
    
    # Save the resized image to the new folder
    cv2.imwrite(data_set_path_safe + image_path, cv2.resize(img, (100, 100)))
    counter += 1
    
print("Out of " + str(len(images_not_safe)) + " images " + str(counter) + " passed the filter in the 'contaminated' folder.")
    

