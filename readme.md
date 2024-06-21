# Canny Edge Detection App

## Overview:
    Given a single image, return the edges of the image using canny edge detection

What i wnat to do is compare different thresholds with canny, this will help me understand thresholding
The goal of this project is to help me understand how thresholding affects canny 

Two directions
1) Option 1 is to input my own thresholds
2) Option 2 is to have a spread of thresholds 
3) be able to add number of images shown?

Hard
4) make a sliding bar illustrating how it is shown 

### Features:
- be able to play with thresholding? 
- Maybe make this a web app? 
- a simple drag and drop onto a file on a web app and it will produce the edges to the right?
- I can implement full stack features this way 



Edge cases:
- accept multiple formats 


Common thresholds 
- 255, 255/3  = 85
-200,100,
250,50



Steps
- Create Virtual env (pip freeze)

- pip install -r requirements.txt



1) is logic for building the canny edge detector, i've done this before

    by the end of 1 i should be able to give an input and return and output 



### Enhancements (Later)
- Adjustable Params
- Multiple Input formats
- Real-Time Processing 
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Edges', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()