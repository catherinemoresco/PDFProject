import numpy as np
import cv2

def rotate(img, angle):
	""" Given an image and angle, returns a rotated copy of the image """
	## Get image width and height
	height = img.shape[0]
	width = img.shape[1]
	## Create transformation matrix
	rotmat = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
	## Return transformed image
	return cv2.warpAffine(img, rotmat, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue = (255, 255, 255))

def horizontal_sums(img):
	""" Return list of sums of pixel values across regularly spaced rows """
	## NumPy function sums rows of image array
	sums=np.sum(img, axis=1)
	return sums

def straighten(img0):
	""" Find rotation angle that maximizes variation of row sums, and returns image rotated at that angle """
	## Create copy of image for processing
	print "straightening..."
	img = np.copy(img0)

	## Convert to grayscale
	if len(img.shape) > 2:
		img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	## Threshold and remove noise by applying morphological filters
	img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 10)
	kernel = np.uint8(np.ones((2,2)))
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.erode(img, kernel, iterations=1)

	## Cast to uint8 type
	img = np.uint8(img)

	## Iterate through range of angles to find maximum row sum variance
	variances = {}
	for x in range(-45, 45, 5):
		variances[np.var(horizontal_sums(rotate(img, x)))] = x
	angle = variances[max(variances.keys())]
	## Iterate through a finer range of values around previous result
	for i in range(angle-5, angle+5):
		variances[np.var(horizontal_sums(rotate(img, i)))] = i
	angle = variances[max(variances.keys())]
	
	## Return image rotated by optimized angle
	return rotate(img0, float(angle))
