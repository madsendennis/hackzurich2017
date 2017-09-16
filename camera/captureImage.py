import picamera
import base64
import time
from flask import Flask

app = Flask(__name__)
camera = picamera.PiCamera()

@app.route("/captureImage")
def captureImage():
    # capture image from camera
    camera.start_preview()
    time.sleep(2)
    camera.capture('cameraImages/Image.jpg')
    camera.stop_preview()

    # convert image to base64 string
    with open('cameraImages/Image.jpg', 'rb') as imageFile:
        str = base64.b64encode(imageFile.read())

    # return base64 representation of image
    return "done"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)