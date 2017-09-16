import picamera
import base64
import time
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import send_file

app = Flask(__name__)
CORS(app, support_credentials=True)
camera = picamera.PiCamera()

@app.route("/captureImage")
@cross_origin(supports_credentials=True)
def captureImage():
    # capture image from camera
    camera.start_preview()
    time.sleep(2)
    camera.capture('cameraImages/Image.jpg')
    camera.stop_preview()

    # convert image to base64 string
    # with open('cameraImages/Image.jpg', 'rb') as imageFile:
    #        str = base64.b64encode(imageFile.read())

    # return base64 representation of image
    #return str

    return send_file('cameraImages/Image.jpg', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)