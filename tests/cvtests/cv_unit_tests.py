import opencv as cv2
import unittest
import page
import line
import document
import pypdf

class all_white_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread("testimg/white.jpg")
        self.document = new_document()
        
    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 0)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, 15)), 15)
    	
    	
class all_black_test_case(unittest.TestCase):

    def setUp(self):
    	#all black image
        self.image = cv2.imread("testimg/black.jpg")
        
    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 0)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, 15)), 15)

    	
class one_picture_test_case(unittest.TestCase):

    def setUp(self):
    	#image
        self.image = cv2.imread("testimg/image.jpg")
        
    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 0)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, 15)), 15)

class perfect_text_test_case(unittest.TestCase):

    def setUp(self):
        # perfect text
        self.image = cv2.imread("testimg/perfecttext.jpg")
        
    def test_merge_text(self):
        #compares number of detected contours to number we observe
        self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
        #compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
        #compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
        self.assertEqual(calculate_angle(self.image), 0)
    
    def test_rotate(self):
        self.assertEqual(calculate_angle(rotate(self.image, 15)), 15)

class text_photo_test_case(unittest.TestCase):

    def setUp(self):
        #image
        self.image = cv2.imread("testimg/textphoto.jpg")
        
    def test_merge_text(self):
        #compares number of detected contours to number we observe
        self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
        #compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
        #compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
        self.assertEqual(calculate_angle(self.image), 0)
    	
    	
class picture_and_text_test_case(unittest.TestCase):

    def setUp(self):
    	#text with image
        self.image = cv2.imread("testimg/perfecttextwithtimage.jpg")
        
    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 0)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, 15)), 15)
    	
class different_sized_test_case(unittest.TestCase):

    def setUp(self):
    	#strangely formatted text
        self.image = cv2.imread("testimg/strangeformatting.jpg")

    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 0)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, 15)), 15)
    

class skewed_pAndT_test_case(unittest.TestCase):

    def setUp(self):
        self.image = cv2.imread("testimg/rotatedwithimage.jpg")
        
    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 15)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, -15)), 0)

    	
class skewed_text_test_case(unittest.TestCase):

    def setUp(self):
        self.image = cv2.imread("testimg/rotated.jpg")
        
    def test_merge_text(self):
    	#compares number of detected contours to number we observe
    	self.assertTrue(cv2.findContours(merge_text(self.image)) <= cv2.findContours(self.image))

    def test_text_area_dilation(self):
    	#compares coordinates of dilated text areas to given coordinates 
        self.assertTrue((text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((text_area_dilation(self.image)[1][1] - 567) < 5)

    def test_non_text_dilation(self):
    	#compares coordinates of dilated non-text areas to given coordinates
        self.assertTrue((non_text_area_dilation(self.image)[0][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[0][1] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][0] - 567) < 5)
        self.assertTrue((non_text_area_dilation(self.image)[1][1] - 567) < 5)
            
    def test_calculate_angle(self):
    	self.assertEqual(calculate_angle(self.image), 15)
    
    def test_rotate(self):
    	self.assertEqual(calculate_angle(rotate(self.image, -15)), 0)



class pdf_reading_test_case(unittest.TestCase):

    def setUp(self):
        self.pdf = PdfFileReader(file("testimg/testpdf.pdf", "rb"))
    
        self.image0 = cv2.imread("testimg/rotatedwithimage.jpg")
        self.image1 = cv2.imread("testimg/textphoto.jpg")
        self.image2 = cv2.imread("testimg/perfecttext.jpg")


    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)[0]), represent_image(self.image0))
        self.assertEqual(represent_image(extract_images(self.pdf)[1]), represent_image(self.image1)) 
        self.assertEqual(represent_image(extract_images(self.pdf)[2]), represent_image(self.image2)) 


if __name__ == '__main__':
    unittest.main()
    