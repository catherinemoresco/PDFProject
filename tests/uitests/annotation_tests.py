from pdfproject import app
from flask import url_for

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#test  5 negative off page text box
class Annotate_Neg_Page(unittest.TestCase):
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

    def test_annotation_creation(self):
        actions = ActionChains(driver)
        actions.click(button)
        actions.move_to_element_with_offset(html, -100, -100)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "textbox") 

    def tearDown(self):
        self.driver.close()

#test  6 large off page text box
class Annotate_Large_Page(unittest.TestCase):
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

    def test_annotation_creation(self):
        actions = ActionChains(driver)
        actions.click(button)
        actions.move_to_element_with_offset(html, 6000, 6000)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "textbox") 

    def tearDown(self):
        self.driver.close()

#test  7 test empty text box
class Annotate_Empty(unittest.TestCase):
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

    def test_annotation_creation(self):
        actions = ActionChains(driver)
        actions.click(button)
        actions.move_to_element_with_offset(html, 50, 50)
        actions.click()
        actions.send_keys(Keys.RETURN)
        actions.perform()
        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "textbox") 

    def tearDown(self):
        self.driver.close()

#test  8 test regular text box
class Annotate_TextBox_Creation(unittest.TestCase):
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

    def test_annotation_creation(self):
        actions = ActionChains(driver)
        actions.click(button)
        actions.move_to_element_with_offset(html, 50, 50)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)
        actions.perform()
        self.assert(actions.find_element_by_id("textbox"))

    def tearDown(self):
        self.driver.close()

#test  9 check text box text
class Annotate_Correct_Text(unittest.TestCase):
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

    def test_annotation_creation(self):
        actions = ActionChains(driver)
        actions.click(button)
        actions.move_to_element_with_offset(html, 300, 50)
        actions.click()
        actions.send_keys("test text box")
        actions.send_keys(Keys.RETURN)
        actions.perform()
        self.assertEqual(actions.find_element_by_id("textbox").get_attribute('value'), "test text box")

    def tearDown(self):
        self.driver.close()



if __name__=="__main":
    unittest.main()
