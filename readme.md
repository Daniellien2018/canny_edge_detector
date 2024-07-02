# Canny Edge Detection App

## Overview:
    Given a single image, return the edges of the image using canny edge detection

## Goals:
- Understand how Canny Edge Detection works via double thresholding and Hysteresis.

- Understand the Guassian Blue Operation in respect to filtering, smoothing, and noise reduction (Hysteresis )

- Visualize Images with edges. 

- Practice application development.

## Potential Future Goals:
- Compare Canny with other Edge Detection Methods (Laplacian, Sobel, Prewitt)
 

Plan:

## MVPs:
- Edge Detector: Given a photo as input, draw edges on the image (Done)

- Threshold Parameters: Be able to adjust thresholding on detection (Done)

- Side by Side Detection: visualize two images side by side, be able to adjust params for this. (Done) 6/28

- 7/1 I want to add a Slider to visualize real time thresholding 7/2
    This sort of works, but fundamentally not sure if the thresholding should be a point of concern--> I cant really tell the difference: This works the first time but doesnt wokr for the second 


#maybe mkae two seperate pages 
## Edge Cases / Issues to Fix

- Error handling for when the file passsed is not an image


Two directions
1) Option 1 is to input my own thresholds
2) Option 2 is to have a spread of thresholds 
3) be able to add number of images shown?

### Features:


### Enhancements (Later)
- Adjustable Params (Done)
- Multiple Input formats
- Real-Time Processing 
- make a sliding bar for threshold adjustment 
- Drag and drop imagesd
- Custom Canny Algorithm from scratch 
- Add an option to decide on the edge detector method, this way I can compare and contract --> make a separate page for each detector 
- Make this like an educational App

Edge Detectioin 
- splash page
--canny
--sobel 
--prewitt
--laplacian


### Steps
- Create Virtual env (pip freeze)

- pip install -r requirements.txt

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Edges', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()