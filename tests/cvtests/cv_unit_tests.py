import cv2 as cv2
import unittest
import getlines
import skew
import extract
import math

##WHAT THESE TESTS DO:
# The first twelve test classes represent different image inputs to the functions within 
# getlines.py and skew.py, which represent the two facets of our processing algorithm.  
# The tests within classes:
#	-test_merge_text: tests basic requirement of getlines.isolateLines (which is our line
#	  getting function comprised of our home-cooked combination of opencv methods), that
#	  our chosen combination of image-processing methods reduces the number of contours 
#	  (simplifies) the image.
#   -test_text_area_dilation: tests more specific requirement of getlines.getLines, that
#     the number of identified lines through our line-getting function are accurate to what
#	  we observe to be the number of lines in the actual image (to within an acceptable 
#     discrepancy)
#   -test_calculate_angle: tests skew.rotate/skew.straighten to make sure that the skew 
#    angle detected by our skew.py functions is equal to the skew angle we observe in the
#    image (to within an acceptable discrepancy).
#    
# The last two test classes represent different .pdf inputs to the functions within 
# extract.py, which represents the processing functionality of page-splitting (splitting
# a multi-page .pdf document into its separate images)
# Tests within class:
#   -test_extract_images: tests that extract.extractImages returns the number of images 
#    that are observed in the document

class all_white_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread("testimg/white.jpg")
        self.lines = getlines.getLines(self.image)
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(getlines.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)
    	
    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue(len(self.lines) == 0)
                   
	#cases with no lines will be presumed to be straight, no rotational testing
    	
    	
class all_black_test_case(unittest.TestCase):

    def setUp(self):
    	#all black image
        self.image = cv2.imread("testimg/black.jpg")
        self.lines = getlines.getLines(self.image)
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(getlines.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)
    	
    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue(len(self.lines) == 0)  
            
	#cases with no lines will be presumed to be straight, no rotational testing

   	
class one_picture_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/image.jpg")
        self.lines = getlines.getLines(self.image)
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(getlines.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
     	print len(self.lines)
        self.assertTrue(abs(len(self.lines) - 0) < 2) 
    
   	#cases with no lines will be presumed to be straight, no rotational testing


class perfect_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/perfecttext.jpg")
        self.lines = getlines.getLines(self.image)
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(getlines.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 18) < 5 and (len(self.lines) - 18) >= 0) 
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertTrue(abs(angle) < 10)


class text_photo_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/textphoto.jpg")
        self.lines = getlines.getLines(self.image)
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(getlines.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.adaptiveThreshold(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY, 11, 2), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 15) < 5 and (len(self.lines) - 15) >= 0) 
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertTrue(abs(angle - 0) < 10)
   	
class picture_and_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/perfecttextwithimage.jpg")
        self.lines = getlines.getLines(self.image)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 35) < 5 and (len(self.lines) - 35) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertTrue(abs(angle - 0) < 2)

class different_sized_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/strangeformatting.jpg")
        self.lines = getlines.getLines(self.image)
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(getlines.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 37) < 5 and (len(self.lines) - 37) >= 0)
     


class skewed_pAndT_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/rotatedwithimage.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = getlines.getLines(self.img)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 35) < 5 and (len(self.lines) - 35) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	self.assertTrue(abs(self.angle - 15) < 2)

    	
class skewed_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/rotated.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = getlines.getLines(self.img)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 18) < 5 and (len(self.lines) - 18) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	self.assertTrue(abs(self.angle + 15) < 2)
 
## added for iteration 2   	

class noisy_text1(unittest.TestCase):

    def setUp(self):
    	#text with background noise (from newspaper)
        self.image = cv2.imread("testimg/noisy1fixed.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = getlines.getLines(self.img)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
     	print len(self.lines)
        self.assertTrue((len(self.lines) - 20) < 5 and (len(self.lines) - 20) >= 0)
        
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	self.assertTrue(abs(self.angle - 3) < 2)
    	
class noisy_text2(unittest.TestCase):

    def setUp(self):
    	#text with one-area noise (from bent corner)
        self.image = cv2.imread("testimg/noisy2fixed.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = getlines.getLines(self.img)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
     	print len(self.lines)
        self.assertTrue(abs(len(self.lines) - 42) < 5)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	self.assertTrue(abs(self.angle + 2) < 2)
    	
class black_margins(unittest.TestCase):

    def setUp(self):
    	#text with large amount of black space from copier error
        self.image = cv2.imread("testimg/blackmarginsfixed.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))    	
        self.lines = getlines.getLines(self.img)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 53) < 5 and (len(self.lines) - 53) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	self.assertTrue(abs(self.angle - 2) < 2)
    	
class long_pdf(unittest.TestCase):

	def setUp(self):
		#specify file path for pdf with 57 images
		self.filepath = "testimg/Biagioli_GalileoCourtier.PDF"
		
	def test_extract_images(self):
		#compares number of images extracted from pdf to number we observe to make sure they are equal
		self.assertTrue(len(extract.extractImages(self.filepath)) == 0)
		

class empty_pdf(unittest.TestCase):

	def setUp(self):
		#specify file path for pdf with 0 images
		self.filepath = "testimg/empty.pdf"
		
	def test_extract_images(self):
		#compares number of images extracted from pdf to number we observe to make sure they are equal
		self.assertTrue(len(extract.extractImages(self.filepath)) == 57)

	
if __name__ == '__main__':
 		unittest.main()
     