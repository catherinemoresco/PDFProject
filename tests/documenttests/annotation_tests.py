import opencv as cv2
import unittest
import page
import line
import document

class annotation_test_case(unittest.TestCase):

	def setUp(self):
		self.annotation = Annotation()
		self.annotation1 = Annotation()


	def test_color(self):
		self.annotation.set_color("#b5b5b5")
		self.assertTrue(self.annotation.get_color() == "#b5b5b5")
		self.annotation.set_color("apple")
		self.assertTrue(self.annotation.get_color() == "#b5b5b5")

	def test_id(self):
		self.assertTrue(self.annotation.get_id() == 0)
		self.assertTrue(self.annotation1.get_id() == 1)

	def test_start_end(self):
		self.annotation.set_topleft((11, 11))
		self.annotation.set_bottomright((100, 100))
		self.annotation1.set_topleft((20, 20))
		self.annotation1.set_bottomright((200, 200))

		self.assertTrue(self.annotation.get_topleft() == (11, 11))
		self.assertTrue(self.annotation.get_bottomright() == (100,100))
		self.assertTrue(self.annotation1.get_topleft() == (20, 20))
		self.assertTrue(self.annotation1.get_bottomright() == (200, 200))


if __name__ == '__main__':
    unittest.main()