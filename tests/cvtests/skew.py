import numpy as np
import cv2

# rotate an image by a given angle
def rotate(img, angle):
	""" Given an image and angle, returns a rotated copy of the image """
	height = img.shape[0]
	width = img.shape[1]
	rotmat = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
	return cv2.warpAffine(img, rotmat, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue = (255, 255, 255))

# get the sum of the values of a row
def horizontal_sums(img):
	""" Return list of sums of pixel values across regularly spaced rows """
	height, width = img.shape
	sums=np.sum(img, axis=1)
	return sums

def straighten(img0):
	""" Find rotation angle that maximizes variation of row sums, and returns image rotated at that angle """
	img = np.copy(img0)
	if len(img.shape) > 2:
		img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	img = np.uint8(img)
	img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 10)

	variances = {}

	# this can be done recurisively, and to greater precision
	# but this works for now
	for x in range(-90, 90, 10):
		variances[np.var(horizontal_sums(rotate(img, x)))] = x
	angle = variances[max(variances.keys())]
	for i in range(angle-10, angle+10):
		variances[np.var(horizontal_sums(rotate(img, i)))] = i
	angle = variances[max(variances.keys())]
	
	return (rotate(img0, angle), angle)
