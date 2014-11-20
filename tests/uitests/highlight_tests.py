from pdfproject import app
from flask import url_for

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Highlight(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        # FIXME
        response = self.driver.get("http://localhost:5000")


    def test_highlight_creation(self):
        # TODO:
        # - click and drag
        # - assert created new highlight

        return

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
