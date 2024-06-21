from flask import Flask, request, render_template, send_file
from edge_detector import EdgeDetector
import cv2
import numpy as np
import io


app = Flask(__name__)
edge_detector = EdgeDetector(threshold1=85, threshold2=255)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # Read the image file
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        # Perform edge detection
        edges = edge_detector.get_edges(image)
        # Save result to a buffer
        _, buffer = cv2.imencode('.jpg', edges)
        io_buf = io.BytesIO(buffer)
        return send_file(io_buf, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
