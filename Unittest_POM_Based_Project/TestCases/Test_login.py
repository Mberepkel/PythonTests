from selenium import webdriver
import unittest
import HtmlTestRunner
import time
import sys
sys.path.append ("C:/Users/VICOMA/PycharmProjects/testing/Unittest_POM_Based_Project/PageObjects/Loginpage.py")
from  Unittest_POM_Based_Project.PageObjects.Loginpage import Loginpage

class Logintest(unittest.TestCase):
    baseurl="https://admin-demo.nopcommerce.com/"
    username= "admin@yourstore.com"
    password="admin"
    driver=webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseurl)
        cls.driver.maximize_window()

    def test_login(self):
        lp=Loginpage(self.driver)
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.setloginbutton(self)
        time.sleep (5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title, "title are not equal")
        lp.setlogout(self)


    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Unittest_POM_Based_Project/Reports"))