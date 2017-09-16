import picamera
import base64
from flask import Flask

app = Flask(__name__)

@app.route("/")
def captureImage():
    # capture image from camera
    camera = picamera.PiCamera()
    camera.capture('cameraImages/Image.jpg')

    # convert image to base64 string
    with open('cameraImages/Image.png', 'rb') as imageFile:
        str = base64.b64encode(imageFile.read())

    # return base64 representation of image
    return "done"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
