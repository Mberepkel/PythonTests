from selenium import webdriver
import unittest
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        self.assertIsNotNone(driver)
        driver = None
        self.assertIsNone(driver)



if __name__==  "__main__":
    unittest.main()