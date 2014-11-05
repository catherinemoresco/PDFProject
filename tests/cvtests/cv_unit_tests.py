import opencv as cv2
import unittest
import page
import line
import document
import pypdf

class all_white_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image1.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document1.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 
    	
    	
class all_black_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image2.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document2.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 
    	
class one_picture_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image3.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document3.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 
    	
    	
class picture_and_text_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image4.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document4.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 
    	
class different_sized_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image5.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document5.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 
    	
class skewed_pAndT_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image6.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document6.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 
    	
class skewed_text_test_case(unittest.TestCase):

    def setUp(self):
    	#all white image
        self.image = cv2.imread(~/image7.jpg)
        self.document = new_document()
        self.pdf = PdfFileReader(file("document7.pdf", "rb"))
        
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
    
    def test_extract_images(self):
    	self.assertEqual(represent_image(extract_images(self.pdf)), represent_image(self.image)) 

if __name__ == '__main__':
    unittest.main()
    