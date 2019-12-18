import unittest

def setUpModule():
    print(" at module bigining")
def tearDownModule():
    print("at module end level")

class Application_setup_up (unittest.TestCase):
    def setUp(self):
        print ("this is setup")

    def tearDown(self):
        print("this is test tear down")

    @classmethod
    def setUpClass(cls):
        print ("this is performed once at begining of the class")

    @classmethod
    def tearDownClass(cls):
        print ("this is performed once at end of class")

    def test_search(self):
        print("this is first test case")

    def test_advanced_search(self):
        print ("this is advanced test case")

    def test_prepaid_search(self):
        print("this is prepaid test case")


if __name__ =="__main__" :
    unittest.main()
