from pdfproject import app
from flask import url_for

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start_url = "http://spark.uchicago.edu/start/"
test_file = "test.pdf"

#test  5 negative off page text box
class Annotation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        filePath = os.getcwd() + test_file
        self.driver.get(start_url)
        uploadF = self.driver.getelement_by_name('fileUpload')
        uploadF.click()
        uploadF.send_keys(filePath)
        elem.send_keys(Keys.RETURN)
        self.driver.getelement_by_name('Submit').click()  
        #response = self.driver.get("http://localhost:5000")

    def test_negative_off_page(self):
        actions = ActionChains(self.driver)

        actions.click(button)
        actions.move_to_element_with_offset(html, -100, -100)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)

        actions.perform()

        self.assertRaises(NoSuchElementException,
                actions.find_element_by_id,
                "textbox")

    def test_large_off_Page(self):
        actions = ActionChains(self.driver)

        actions.click(button)
        actions.move_to_element_with_offset(html, 6000, 6000)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)

        actions.perform()

        self.assertRaises(NoSuchElementException, 
                actions.find_element_by_id, 
                "textbox")

    def test_empty_text(self):
        actions = ActionChains(self.driver)

        actions.click(button)
        actions.move_to_element_with_offset(html, 50, 50)
        actions.click()
        actions.send_keys(Keys.RETURN)

        actions.perform()

        self.assertRaises(NoSuchElementException,
                actions.find_element_by_id,
                "textbox")

    def test_valid_text(self):
        actions = ActionChains(self.driver)

        actions.click(button)
        actions.move_to_element_with_offset(html, 50, 50)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)

        actions.perform()

        textbox = actions.find_element_by_id("textbox")

        self.assert(textbox)
        self.assertEqual(textbox.get_attribute('value'), "test text box")

    def tearDown(self):
        self.driver.close()

if __name__=="__main":
    unittest.main()
