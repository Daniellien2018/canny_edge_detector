from flask import Flask, request, render_template
from edge_detector import EdgeDetector
import cv2
import numpy as np
import base64
import io

app = Flask(__name__)

def to_base64(image):
    """Convert image to base64."""
    _, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer).decode('utf-8')

# Register the custom filter
app.jinja_env.filters['to_base64'] = to_base64

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
        # Get the threshold values for both pairs
        threshold1_1 = int(request.form.get('threshold1_1', 50))
        threshold2_1 = int(request.form.get('threshold2_1', 250))
        threshold1_2 = int(request.form.get('threshold1_2', 100))
        threshold2_2 = int(request.form.get('threshold2_2', 200))
        
        # Initialize edge detectors for both threshold pairs
        edge_detector1 = EdgeDetector(threshold1=threshold1_1, threshold2=threshold2_1)
        edge_detector2 = EdgeDetector(threshold1=threshold1_2, threshold2=threshold2_2)
        
        # Read the image file
        image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
        # Perform edge detection with both sets of thresholds
        edges1 = edge_detector1.get_edges(image)
        edges2 = edge_detector2.get_edges(image)

        edges1_base64 = to_base64(edges1)
        edges2_base64 = to_base64(edges2)

        return render_template('show.html', edges1=edges1_base64, edges2=edges2_base64, 
                               threshold1_1=threshold1_1, threshold2_1=threshold2_1,
                               threshold1_2=threshold1_2, threshold2_2=threshold2_2)
if __name__ == '__main__':
    app.run(debug=True)
