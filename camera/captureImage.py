import picamera
import base64
from flask import Flask

app = Flask(__name__)

@app.route("/captureImage")
def captureImage():
    return "done"

if __name__ == "__main__":
    app.run(host='', port=5000)
