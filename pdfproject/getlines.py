import cv2
import numpy as np
import json

 ## Definitions of kernels for transformations
kernel = np.uint8(np.ones((2,2)))
kernelbig = np.uint8(np.ones((5,5)))
kernelrowsmall = np.float32(np.ones((1, 25)))/25
kernelrow = np.float32(np.ones((1, 50)))/50


def isolateLines(end):
	""" Filter image to return a new image with blocked-out boxes where lines of text are located """

## Convert image to grayscale	
	if (len(end.shape) == 3):
	  end = cv2.cvtColor(end, cv2.COLOR_BGR2GRAY)

## Running image through filters should result in an image with boxes
## that correspond to positions of original text lines.

## Sobel derivative (in x direction)
	end = cv2.Sobel(end, cv2.CV_8U, 1, 0, ksize=1)
## Threshold image:
  	ret, end = cv2.threshold(end, 50, 255, cv2.THRESH_BINARY)
## Erode and then dilate, to remove noise
	end = cv2.erode(end, kernel, iterations=1)
	end = cv2.dilate(end, kernelbig, iterations=1)
## Apply line filter:
	end = cv2.filter2D(end, -1, kernelrow)
## Final threshold and erosion
	ret, end = cv2.threshold(end, 20, 255, cv2.THRESH_BINARY)
	end = cv2.erode(end, kernelrow, iterations=3)
  
	return end

def getLines(inputimg):
  """ Return a list of tuples corresponding to the upper left and lower right corners of bounding boxes of lines """

  ## Get image with isolated lines
  img = isolateLines(inputimg)

  ## OpenCV functionr returns polygons which correspond to image features.
  contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  lines = {}

  for i in range(0, len(contours)):
  	## Area threshold to eliminate noise features
  	if cv2.contourArea(contours[i]) > 500:
  		## Getting bounding rect of each line to eliminate contour irregularities
  		x, y, w, h = cv2.boundingRect(contours[i])
  		lines[i] = ((x, y), (x+w, y+h))

  ## Return a list with tuples that represent bounding rects
  return lines
