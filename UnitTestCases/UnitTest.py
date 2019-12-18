import unittest
from selenium import webdriver

class Googlesearch(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http:google.co.uk")
        print("title of the page is :" + self.driver.title)
        self.driver.close()

class BingSearch(unittest.TestCase):
    def test_Bing(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http:bing.com")
        print("title of the page is :" + self.driver.title)
        self.driver.close()

if __name__=='__main__':
        unittest.main()
