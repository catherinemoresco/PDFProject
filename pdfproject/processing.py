import extract
import skew
import getlines
import cv2

def process(pdf):
	images = extract.extractImages(pdf)
	# map(skew.straighten, images)
	map(getlines.getLines, images)
	n=1
	for i in images:
		p = pdf+str(n)+".jpg"
		cv2.imwrite(p,i)
		n = n+1
  #return images
