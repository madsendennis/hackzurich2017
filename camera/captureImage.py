import picamera
from flask import Flask
app = Flask(__name__)

@app.route("/captureImage")
def captureImage():
    camera = picamera.PiCamera()
    camera.capture('cameraImages/Image.jpg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)