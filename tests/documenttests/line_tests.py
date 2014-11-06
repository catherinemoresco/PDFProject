import opencv as cv2
import unittest
import page
import line
import document

class line_test_case(unittest.TestCase):

	def setUp(self):
		self.line = Line((0, 0), (50, 10), 1)
		self.highlight = Highlight()

	def test_init(self):
		self.assertTrue(self.line.upperLeft == (0,0))
		self.assertTrue(self.line.bottomRight == (50, 10))
		self.assertEqual(self.lineID, 1)
		self.assertTrue(self.highlights == [])

	def test_add_highlight(self):
		self.assertTrue(self.line.addHighlight(self.highlight))
		self.assertEqual(len(self.line.highlights), 1)

if __name__ == '__main__':
    unittest.main()