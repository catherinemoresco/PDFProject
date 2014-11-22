import extract
import skew
import getlines
import cv2

def process(pdf):
	largest_ratio = 0
	images = extract.extractImages(pdf)
	# images = [skew.straighten(i) for i in images]
	n=1
	print "images found: " + str(len(images))
	for i in images:
		ratio = float(i.shape[0])/float(i.shape[1])
		if ratio > largest_ratio:
			largest_ratio = ratio
		p = pdf+str(n)+".jpg"
		cv2.imwrite(p,i)
		n = n+1
	return largest_ratio*100
