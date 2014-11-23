import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Upload(unittest.TestCase)
    start_url            = "http://spark.uchicago.edu/start/"

    name_btn_file_upload = "fileUpload"
    name_btn_submit      = "Submit"
    

    def setUp(self):
        driver = webdriver.Chrome()


    def test_valid(self):
        file_path_valid = os.getcwd() +'test.pdf'

        driver.get(Upload.start_url)

        driver.getelement_by_name(Upload.name_btn_file_upload).click()

        uploadF.send_keys(file_path_valid)
        elem.send_keys(Keys.RETURN)

        driver.getelement_by_name(Upload.name_btn_submit).click()

        assert "File Upload Success" in driver.page_source


    def test_blank_name(self):
        driver.get(Upload.start_url)

        driver.getelement_by_name(Upload.name_btn_file_upload).click()

        uploadF.send_keys("")
        elem.send_keys(Keys.RETURN)

        driver.getelement_by_name(Upload.name_btn_submit).click()

        assert "File Upload Success" not in driver.page_source


    def test_invalid_file_format(self):
        file_path_invalid = os.getcwd() +'test.jpg'

        driver.get(Upload.start_url)

        driver.getelement_by_name(Upload.name_btn_file_upload).click()

        uploadF.send_keys(file_path_invalid)
        elem.send_keys(Keys.RETURN)

        driver.getelement_by_name(Upload.name_btn_submit).click()

        assert "File Upload Success" not in driver.page_source		


    def tearDown(self);
        driver.close()


if __name__ == "__main__":
    unittest.main()
