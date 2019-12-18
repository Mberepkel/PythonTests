import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.get("https://google.co.uk")
        title_of_page = driver.title
        print(title_of_page)
        #self.assertTrue(title_of_page == "Google")
        self.assertFalse(title_of_page == "Google123")


if __name__==  "__main__":
    unittest.main()