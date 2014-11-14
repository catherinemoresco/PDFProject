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
	pages = []
	images = extractImages(pdfPath)
	for i in images:
		straightImage= straigthen(i)
		outImage,lines = getLines(straightImage)
		pages.append((outImage,lines))
	return pages