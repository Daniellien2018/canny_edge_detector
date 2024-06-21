import os
import cv2
import matplotlib.pyplot as plt
from canny_edge_app.edge_detector import EdgeDetector
from pathlib import Path



### Define input and output folder paths using pathlib
input_folder_path = Path('/home/daniel/dev/canny_edge_detection/input')
output_folder_path = Path('/home/daniel/dev/canny_edge_detection/output')

# Ensure the output directory exists
output_folder_path.mkdir(parents=True, exist_ok=True)


#Initialize the edge detector; can also initialize without params, will default to 100,200 set in class 
edge_detector = EdgeDetector(threshold1=85, threshold2=255)


for image_file in input_folder_path.iterdir():
    if image_file.is_file() and image_file.suffix in ['.jpg', '.png', '.jpeg']:
        image = cv2.imread(str(image_file), cv2.IMREAD_GRAYSCALE)  
        edges = edge_detector.get_edges(image)
        
        # Define the output file path
        output_path = output_folder_path / f"{image_file.stem}_edges{image_file.suffix}"
        edge_detector.save_image(edges, str(output_path))
