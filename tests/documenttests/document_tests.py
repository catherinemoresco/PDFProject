import opencv as cv2
import unittest
import page
import line
import document

class page_test_case(unittest.TestCase):

	def setUp(self):
		self.image1 = cv2.imread("/tests/testimg/perfecttext.jpg")
        self.image2 = cv2.imread("/tests/testimg/black.jpg")
   		images = [image1, image2]
		self.doc = Document("thisisthename", self.images)


	def test_init(self):
		doc = Document("thisisthename", self.images)
		self.assertTrue(doc.name == "thisisthename")
		self.assertEqual(len(doc.images), 2)
		self.assertTrue(doc.images[0], doc.images[1] == self.image1, self.image2)

	def test_set_name(self):
		(self.doc).set_name("thisisanewname123")
		self.assertTrue(self.name == "thisisanewname")
		(self.doc).set_name("thisthename")
		self.assertTrue(self.name == "thisisthename")



if __name__ == '__main__':
    unittest.main()