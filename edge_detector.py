import cv2
import matplotlib.pyplot as plt

class EdgeDetector:
    """Class for the Edge Detector"""
    def __init__(self, threshold1, threshold2, blur_ksize=(5,5)):
        """
        Initialize the Edge Detector with default threshold values for Canny Edge Detector
        
        Args:
            threshold1 (int): First threshold for the hysteresis procedure
            threshold2 (int): Second threshold for the hytseresis procedure
        """
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        self.blur_ksize = blur_ksize

    def get_edges(self, image):
        """
        Finds the edges on an image using Canny Edge Detection
        
        Args:
            image (numpy.ndarray): Image data as a NumPy array.
        Returns: 
            edges (numpy.ndarray): Edge-detected image as NumPy array.
        """
        blurred_image = cv2.GaussianBlur(image, self.blur_ksize, 0)
        edges = cv2.Canny(blurred_image, self.threshold1, self.threshold2 )
        return edges
    
    def set_thresholds(self, threshold1, threshold2):
        """
        Set the thresholds for the Canny Edge Detection.
        
        Args:
            threshold1 (int): First threshold for the hysteresis procedure.
            threshold2 (int): Second threshold for the hysteresis procedure.
        """
        self.threshold1 = threshold1
        self.threshold2 = threshold2

    def display_image(self, image, title='Image'):
        """
        Display an image using matplotlib.
        
        Args:
            image (numpy.ndarray): Image data as a NumPy array.
            title (str): Title of the displayed image.
        """
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.axis('off')
        plt.show()

    def save_image(self, image, path):
        """
        Save an image to the specified path.
        
        Args:
            image (numpy.ndarray): Image data as a NumPy array.
            path (str): Path to save the image.
        """
        cv2.imwrite(path, image)


#How can i write unit tests for this class? can do later 