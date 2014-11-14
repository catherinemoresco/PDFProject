import PythonMagick
import PyPDF2
import numpy as np 
import base64
import cv2
import StringIO
import json
import processing  
import skew 
import extract 

def processPDF(pdfPath):
	processedImages = []
	images = extract.extractImages(pdfPath)
	fpath = pdfPath + '.txt'
	f = open(fpath,'w')
	f.write('hi there\n') # python will convert \n to os.linesep
	f.close() # you can omit in most cases as the destructor will call if
'''
	for i in images:
		straightImage= skew.straigthen(i)
		outImage,lines = processing.getLines(straightImage)
		processedImages.append((outImage,lines))
	#for p in processedImages:
	#	p[0]
'''