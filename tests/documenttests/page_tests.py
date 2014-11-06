import opencv as cv2
import unittest
import page
import line
import document

class page_test_case(unittest.TestCase):

	def setUp(self):
		self.image1 = cv2.imread("/tests/testimg/perfecttext.jpg")
		self.page = Page(self.image1, 1)
		self.annotation = Annotation()

	def test_init(self):
		self.assertTrue(self.page.image = self.image1)
		self.assertEqual(self.width, image1.shape[1])
		self.assertEqual(self.height, image1.shape[0])
		self.assertEqual(self.pageNumber, 1)
		self.assertEqual(len(self.lines), 18)
		self.assertTrue(self.edits == [])

	def test_add_annotation(self):
		self.assertTrue(self.page.addAnnotation(self.annotation))
		self.assertEqual(len(self.page.edits), 1)

if __name__ == '__main__':
    unittest.main()