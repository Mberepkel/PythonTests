from selenium import webdriver
import unittest

class Test(unittest.TestCase):
    def test_Name(self):
        driver = webdriver.Chrome()
        driver.get("https://google.co.uk")
        title_of_page=driver.title
        self.assertEqual("Google",title_of_page,"webpage title are not same")
        #self.assertNotEqual("Google123",title_of_page,"page is the same")

if __name__=='__main__':
    unittest.main()