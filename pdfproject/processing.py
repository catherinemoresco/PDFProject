import cv2

## image processing algorithm based on QI Xiaorui, 
## MA Lei, LIU Jiang, and SUN Changjiang, "Fast Skew Angle
## Detection Algorithm for Scanned Document Images"

## import test image (development purposes only)
test = cv2.imread("perfecttext.jpg")

## step 1: convert to black and white

## step 2: horizontal gradient

## step 3: merge text areas

## step 4: filter text areas

## step 5: filter non-text areas

## step 6: identify lines


window = cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", test)
cv2.waitKey(0)
cv2.destroyAllWindows()