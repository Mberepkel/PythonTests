from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRM(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_Homepagetitle(self):
        self.driver.get("https://google.com/")
        self.assertEqual("Google",self.driver.title, "title does not match")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "title does not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print ("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../testing/Reporting"))
    ## run in terminal or cmd to get report file C:\Users\VICOMA\PycharmProjects\testing>python  HTMLUnittest/Test_Orange_login.py

