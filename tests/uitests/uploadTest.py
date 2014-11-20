import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Highlight(unittest.TestCase)
    def setUp(self):
        driver = webdriver.Chrome()
	def test_upload(self)
		filePath = os.getcwd() +'test.pdf'
		
		#Correct File Upload
		driver.get("http://spark.uchicago.edu/start/")
		uploadF = driver.getelement_by_name('fileUpload')
		uploadF.click()
		uploadF.send_keys(filePath)
		elem.send_keys(Keys.RETURN)
		driver.getelement_by_name('Submit').click()
		assert "File Upload Success" in driver.page_source
		
		#Blank name entered
		driver.get("http://spark.uchicago.edu/start/")
		uploadF = driver.getelement_by_name('fileUpload')
		uploadF.click()
		uploadF.send_keys("")
		elem.send_keys(Keys.RETURN)
		driver.getelement_by_name('Submit').click()
		assert "File Upload Success" not in driver.page_source

		#Not a PDF uploaded
		filePath = os.getcwd() +'test.jpg'
		driver.get("http://spark.uchicago.edu/start/")
		uploadF = driver.getelement_by_name('fileUpload')
		uploadF.click()
		uploadF.send_keys("")
		elem.send_keys(Keys.RETURN)
		driver.getelement_by_name('Submit').click()
		assert "File Upload Success" not in driver.page_source		
		
	
	def tearDown(self);
        driver.close()
if __name__ == "__main__":
    unittest.main()
