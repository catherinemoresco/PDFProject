from pdfproject import app
from flask import url_for

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Highlight(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        filePath = os.getcwd() +'test.pdf'
        driver.get("http://spark.uchicago.edu/start/")
        uploadF = driver.getelement_by_name('fileUpload')
        uploadF.click()
        uploadF.send_keys(filePath)
        elem.send_keys(Keys.RETURN)
        driver.getelement_by_name('Submit').click()
        #response = self.driver.get("http://localhost:5000")


    def test_negative_off_page(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, -100, -100)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 0, 0)
        actions.release()
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 

    def test_large_off_page(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, 6000, 6000)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 7000, 7000)
        actions.release()
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 

    def test_zero_size(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, 0, 0)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 0, 0)
        actions.release()
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 

    def test_valid(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, 300, 300)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 400, 400)
        actions.release()
        actions.perform()
        self.assert(actions.find_element_by_id("highlight"))

    def tearDown(self):
        self.driver.close()
