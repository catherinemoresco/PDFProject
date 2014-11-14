import numpy as np
from scipy import misc
import cv2

# rotate an image by a given angle
def rotate(img, angle):
	height, width = img.shape[0], img.shape[1]
	rotmat = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
	return cv2.warpAffine(img, rotmat, (width, height))

# get the sum of the values of a row
def horizontal_sums(img):
	height, width = img.shape[0], img.shape[1]
	sums = []
	for i in range(0+(height/25), height-(height/25), (height/10)):
		sums.append(sum(img[i]))
	return sums

# rotate an image by an angle that maximizes the standard deviation of its row sums
def straighten(img):
	stds = {}

	# this can be done recurisively, and to greater precision
	# but this works for now
	for x in range(-90, 90, 10):
		stds[np.std(horizontal_sums(rotate(img, x)))] = x
	angle = stds[max(stds.keys())]
	for i in range(angle-5, angle+5):
		stds[np.std(horizontal_sums(rotate(img, i)))] = i
	angle = stds[max(stds.keys())]

	return rotate(img, angle)

window = cv2.namedWindow("image", cv2.WINDOW_NORMAL)
img = cv2.imread("rotatedwithimage.jpg")
test = straighten(img)
cv2.imshow("image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()