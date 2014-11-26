import extract
import skew
import getlines
import cv2
import json


def process(pdf):
	""" Extract images, fix skew, and get line positions, writing images and data to files. There is no return value."""
	images = extract.extractImages(pdf)
	lines = {} 
	# images = [skew.straighten(i) for i in images]
	n=1
	print "images found: " + str(len(images))
	for i in images:
		p = pdf+str(n)+".jpg"
		lines[n]=getlines.getLines(i)
		cv2.imwrite(p,i)
		n = n+1
	with open ((pdf+".json.txt"),'w') as outfile:
		json.dump(lines,outfile)
