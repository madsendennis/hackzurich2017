import picamera
import base64
import time
from flask import Flask, Response
from flask_cors import CORS, cross_origin
from flask import send_file
import os.path

app = Flask(__name__)
CORS(app, support_credentials=True)
camera = picamera.PiCamera()
camera.resolution = (800, 600)

@app.route("/captureImage")
@cross_origin(supports_credentials=True)
def captureImage():
    camera.capture('cameraImages/Image.jpg')    
    return send_file('cameraImages/Image.jpg', mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
