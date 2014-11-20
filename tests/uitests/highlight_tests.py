from pdfproject import app
from flask import url_for

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#test  1 negative off page highlight
class Highlight_Neg_Page(unittest.TestCase):
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


    def test_highlight_creation(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, -100, -100)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 0, 0)
        actions.release()
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 

        

    def tearDown(self):
        self.driver.close()

#test  2 large off page highlight
class Highlight_Large_Page(unittest.TestCase):
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


    def test_highlight_creation(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, 6000, 6000)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 7000, 7000)
        actions.release()
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 
        

    def tearDown(self):
        self.driver.close()

#test  3 no movement highlight
class Highlight_No_Move(unittest.TestCase):
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


    def test_highlight_creation(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, 0, 0)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 0, 0)
        actions.release()
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 

        
    def tearDown(self):
        self.driver.close()

#test  4 working highlight
class Highlight_Good_Highlight(unittest.TestCase):
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


    def test_highlight_creation(self):
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(html, 300, 300)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 400, 400)
        actions.release()
        actions.perform()
        self.assert(actions.find_element_by_id("highlight"))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
