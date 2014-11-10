import cv2
import numpy as np

## image processing algorithm based on QI Xiaorui, 
## MA Lei, LIU Jiang, and SUN Changjiang, "Fast Skew Angle
## Detection Algorithm for Scanned Document Images"

## import test image (development purposes only)
test = cv2.imread("testimg/textphoto.jpg")
test2 = cv2.imread("testimg/perfecttextwithimage.jpg")


kernel = np.uint8(np.ones((2,2)))
kernelbig = np.uint8(np.ones((5,5)))

kernelrowsmall = np.float32(np.ones((1, 25)))/25
kernelrow = np.float32(np.ones((1, 50)))/50


## step 1: convert to black and white

## accidentally combined many steps into one big function for now
def convertToBW(img):
	end = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sobel derivative (in x direction):
	end = cv2.Sobel(end, cv2.CV_8U, 1, 0, ksize=1)

##	threshold image:
  	ret, end = cv2.threshold(end, 50, 255, cv2.THRESH_BINARY)

# ## erode and then dilate, to remove noise
	end = cv2.erode(end, kernel, iterations=1)
	end = cv2.dilate(end, kernelbig, iterations=1)

	end = cv2.filter2D(end, -1, kernelrow)
	ret, end = cv2.threshold(end, 20, 255, cv2.THRESH_BINARY)
	end = cv2.erode(end, kernelrow, iterations=3)


	return end

## step 2: horizontal gradient

## step 3: merge text areas

## step 4: filter text areas

## step 5: filter non-text areas

## step 6: identify lines


img = convertToBW(test)


#show image (development purposes only)
window = cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()