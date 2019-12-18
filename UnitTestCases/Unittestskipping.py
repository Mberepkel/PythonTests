from selenium import webdriver
import unittest

class Application_setup_up (unittest.TestCase):
    #def setUp(self):
        #print ("this is setup")

    #def tearDown(self):
        #print("this is test tear down")
    @unittest.SkipTest
    def test_search(self):
        print("this is first search test case")
    @unittest.skip("test not ready")
    def test_advancedsearch(self):
        print ("this is advanced search test case")

    @unittest.skipIf(1==1,"1 is equal to 1")
    def test_prepaidsearch(self):
        print("this is prepaid test case")

    def test_postpaysearch(self):
        print("this is postpay search")

    def test_loginbytwiter(self):
        print ("this is twiter log in")

    def test_loginbygmail(self):
        print ("this is gmail log in")

if __name__== "__main__":
    unittest.main()
