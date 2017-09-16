import picamera
import base64
import time
from flask import Flask

app = Flask(__name__)

@app.route("/captureImage")
def captureImage():
    # capture image from camera
    camera = picamera.PiCamera()
    camera.start_preview()
    camera.capture('cameraImages/Image.jpg')
    time.sleep(2)

    # convert image to base64 string
    with open('cameraImages/Image.jpg', 'rb') as imageFile:
        str = base64.b64encode(imageFile.read())

    # return base64 representation of image
    return "done"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
