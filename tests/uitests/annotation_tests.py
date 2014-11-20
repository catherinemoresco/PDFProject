import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Annotate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_annotation_creation(self):
        # TODO:
        # - click
        # - assert created new annotation

        return

    def tearDown(self):
        self.driver.close()

if __name__=="__main":
    unittest.main()
