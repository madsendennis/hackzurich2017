import base64
from flask import Flask

app = Flask(__name__)

@app.route("/receiveImage", methods=['POST'])
def receiveImage():
    # Read base64 representation of Image
    imageString = request.form.get('imageString')

    # Convert to jpeg image
    fh = open("receivedImage.jpg", "wb")
    fh.write(imageString.decode('base64'))
    fh.close()

    # Call the contamination detection logic here


    # Generate Report


    # Return Report
    return "the best report ever - will be a JSON string."

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
