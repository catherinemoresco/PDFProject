import cv2
import numpy as np
import json

# for testing
#img = cv2.imread("Bennett_MechanicsPhilosophy.pdf2.jpg")

kernel = np.uint8(np.ones((2,2)))
kernelbig = np.uint8(np.ones((5,5)))

kernelrowsmall = np.float32(np.ones((1, 25)))/25
kernelrow = np.float32(np.ones((1, 50)))/50


def isolateLines(end):
	end = cv2.cvtColor(end, cv2.COLOR_BGR2GRAY)

# sobel derivative (in x direction):
	end = cv2.Sobel(end, cv2.CV_8U, 1, 0, ksize=1)

##	threshold image:
  	ret, end = cv2.threshold(end, 50, 255, cv2.THRESH_BINARY)

## erode and then dilate, to remove noise
	end = cv2.erode(end, kernel, iterations=1)
	end = cv2.dilate(end, kernelbig, iterations=3)

	end = cv2.filter2D(end, -1, kernelrow)
	ret, end = cv2.threshold(end, 1, 255, cv2.THRESH_BINARY)
	end = cv2.erode(end, kernelrow, iterations=5)


	end = cv2.dilate(end, kernelrow, iterations=5)
  


	return end

def getLines(inputimg):
  img = isolateLines(inputimg)
  contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  lines = {}
  # for testing:
  # cv2.drawContours(inputimg, contours, -1, (0, 255, 0), 3)
  # cv2.namedWindow("w")
  # cv2.imshow("w", inputimg)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  for i in range(0, len(contours)):
  	if cv2.contourArea(contours[i]) > 500:
  		x, y, w, h = cv2.boundingRect(contours[i])
  		lines[i] = ((x, y), (x+w, y+h))

  return lines
