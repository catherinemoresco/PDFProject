import extract
import skew
import getlines
import cv2

def process(pdf):
	images = extract.extractImages(pdf)
	images = [skew.straighten(i) for i in images]
	n=1
	for i in images:
		p = pdf+str(n)+".jpg"
		cv2.imwrite(p,i)
		n = n+1
	return images
