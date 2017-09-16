import picamera

# Capture Image to file 
def captureImage():
    camera = picamera.PiCamera()
    camera.capture('cameraImages/Image.jpg')

if __name__ == "__main__":
    captureImage()