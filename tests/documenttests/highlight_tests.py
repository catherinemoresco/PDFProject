import opencv as cv2
import unittest
import page
import line
import document

class highlight_test_case(unittest.TestCase):

	def setUp(self):
		self.highlight  = Highlight(11, 100)
		self.highlight1 = Highlight(22, 200)

	def test_color(self):
		color      = "#b5b5b5"
                color_name = "apple"

                self.highlight.set_color(color)
		self.assertTrue(self.highlight.get_color() == color)
		self.highlight.set_color(color_name)
		self.assertTrue(self.highlight.get_color() == color)

	def test_color(self):
		self.highlight.set_background_color("#b5b5b5")
		self.assertTrue(self.highlight.get_background_color() == "#b5b5b5")
		self.highlight.set_background_color("apple")
		self.assertTrue(self.highlight.get_background_color() == "#b5b5b5")

	def test_id(self):
		self.assertTrue(self.highlight.get_id() == 0)
		self.assertTrue(self.highlight1.get_id() == 1)

	def test_start_end(self):
		self.assertTrue(self.highlight.get_start() == 11)
		self.assertTrue(self.highlight.get_end() == 100)
		self.assertTrue(self.highlight1.get_start() == 22)
		self.assertTrue(self.highlight1.get_end() == 200)


	def test_content(self):
		self.highlight.set_content("Hello, world")
		self.assertTrue(self.highlight.get_content() == "Hello world")
		self.highlight.set_content("Hello, moon")
		self.assertTrue(self.highlight.get_content() == "Hello moon")


if __name__ == '__main__':
    unittest.main()
