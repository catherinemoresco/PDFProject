import cv2 as cv2
import unittest
#import pypdf
import processing
#import extract
import skew
import json
import math

class all_white_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread("testimg/white.jpg")
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
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
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
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
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue(len(self.lines) == 0) 
    
   	#cases with no lines will be presumed to be straight, no rotational testing


class perfect_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/perfecttext.jpg")
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 18) < 5 and (len(self.lines) - 18) >= 0) 
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	print angle
    	self.assertTrue(abs(angle) < 10)


class text_photo_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/textphoto.jpg")
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.adaptiveThreshold(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY, 11, 2), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 15) < 5 and (len(self.lines) - 15) >= 0) 
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	print angle
    	self.assertTrue(abs(angle - 0) < 10)
   	
class picture_and_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/perfecttextwithimage.jpg")
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 35) < 5 and (len(self.lines) - 35) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	print angle
    	self.assertTrue(abs(angle - 0) < 2)

class different_sized_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/strangeformatting.jpg")
        self.lines = json.loads(processing.getLines(self.image)[1])
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
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
        self.lines = json.loads(processing.getLines(self.img)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.img), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(self.img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 35) < 5 and (len(self.lines) - 35) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	print self.angle
    	self.assertTrue(abs(self.angle - 15) < 2)

    	
class skewed_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/rotated.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = json.loads(processing.getLines(self.img)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.img), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(self.img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 18) < 5 and (len(self.lines) - 18) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	print self.angle
    	self.assertTrue(abs(self.angle + 15) < 2)
 
## added for iteration 2   	

class noisy_text1(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/noisy1.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = json.loads(processing.getLines(self.img)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.img), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 20) < 5 and (len(self.lines) - 20) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	print self.angle
    	self.assertTrue(abs(self.angle - 4) < 2)
    	
class noisy_text2(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/noisy2.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = json.loads(processing.getLines(self.img)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.img), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 44) < 5 and (len(self.lines) - 44) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	print self.angle
    	self.assertTrue(abs(self.angle + 2) < 2)
    	
class black_margins(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/blackmargins.jpg")
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.lines = json.loads(processing.getLines(self.img)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.img), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        self.assertTrue((len(self.lines) - 46) < 5 and (len(self.lines) - 46) >= 0)
    
    def test_calculate_angle(self):
    	#compares calculated angle to observed angle to make sure they are equal
    	print self.angle
    	self.assertTrue(abs(self.angle - 2) < 2)

	
if __name__ == '__main__':
 		unittest.main()
     