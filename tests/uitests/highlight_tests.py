import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Highlight(unittest.TestCase):
    start_url            = "http://spark.uchicago.edu/start/"

    name_btn_file_upload = "fileUpload"
    name_btn_submit      = "Submit"


    def setUp(self):
        file_path_valid = os.getcwd() +'test.pdf'

        self.driver = webdriver.Chrome()
        self.driver.get(Highlight.start_url)
        uploadF = self.driver.getelement_by_name(Highlight.name_btn_file_upload)
        uploadF.click()
        uploadF.send_keys(file_path_valid)
        elem.send_keys(Keys.RETURN)
        self.driver.getelement_by_name('Submit').click()


    def test_negative_off_page(self):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(html, -100, -100)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 0, 0)
        actions.release()

        actions.perform()

        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 


    def test_large_off_page(self):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(html, 6000, 6000)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 7000, 7000)
        actions.release()

        actions.perform()

        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 


    def test_zero_size(self):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(html, 0, 0)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 0, 0)
        actions.release()

        actions.perform()

        self.assertRaises(NoSuchElementException, actions.find_element_by_id, "highlight") 


    def test_valid(self):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(html, 300, 300)
        actions.click_and_hold()
        actions.move_to_element_with_offset(html, 400, 400)
        actions.release()

        actions.perform()

        self.assert(actions.find_element_by_id("highlight"))


    def tearDown(self):
        self.driver.close()
