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
        print len(self.lines)
        self.assertTrue(len(self.lines) == 0)
                   
    def test_calculate_angle(self):
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertEqual(abs(angle - 0) < 2)
    	
    	
class all_black_test_case(unittest.TestCase):

    def setUp(self):
    	#all black image
        self.image = cv2.imread("testimg/black.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)
    	
    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue(len(self.lines) == 0)  
            
    def test_calculate_angle(self):
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertEqual(abs(angle - 0) < 2)

   	
class one_picture_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/image.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue(len(self.lines) == 0) 
    
    def test_calculate_angle(self):
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertEqual(abs(angle - 0) < 2)


class perfect_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/perfecttext.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue((len(self.lines) - 18) < 5 and (len(self.lines) - 18) >= 0) 
    
    def test_calculate_angle(self):
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertEqual(abs(angle - 0) < 2)


class text_photo_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/textphoto.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue((len(self.lines) - 15) < 5 and (len(self.lines) - 15) >= 0) 
    
    def test_calculate_angle(self):
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertEqual(abs(angle - 0) < 2)
   	
class picture_and_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/perfecttextwithimage.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue((len(self.lines) - 35) < 5 and (len(self.lines) - 35) >= 0)
    
    def test_calculate_angle(self):
    	img, angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
    	self.assertEqual(abs(angle - 0) < 2)

class different_sized_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/strangeformatting.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue((len(self.lines) - 37) < 5 and (len(self.lines) - 37) >= 0)
    
    def test_calculate_angle(self):
    	self.assertEqual(abs(self.angle - 0) < 2)


class skewed_pAndT_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/rotatedwithimage.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue((len(self.lines) - 35) < 5 and (len(self.lines) - 35) >= 0)
    
    def test_calculate_angle(self):
    	self.assertEqual(abs(self.angle - 15) < 2)
    
    def test_rotate(self):
    	self.assertEqual(abs(self.img - 0) < 2)

    	
class skewed_text_test_case(unittest.TestCase):

    def setUp(self):
    	#one picture image
        self.image = cv2.imread("testimg/rotated.jpg")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.lines = json.loads(processing.getLines(self.image)[1])
        self.img, self.angle = skew.straighten(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        
    def test_merge_text(self):
    	#makes sure number of contours is decreasing through processing
    	after_len = len(cv2.findContours(processing.isolateLines(self.image), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	before_len = len(cv2.findContours(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0])
    	self.assertTrue(after_len <= before_len)

    def test_text_area_dilation(self):
     	#compares number of detected lines to number we observe to make sure they are equal
        print len(self.lines)
        self.assertTrue((len(self.lines) - 18) < 5 and (len(self.lines) - 18) >= 0)
    
    def test_calculate_angle(self):
    	self.assertEqual(abs(self.angle - 15) < 2)
    
    def test_rotate(self):
    	self.assertEqual(abs(self.img - 0) < 2)

	
if __name__ == '__main__':
 		unittest.main()
     