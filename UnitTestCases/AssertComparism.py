#relational comparison
import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        self.assertGreater(100,10,)  ## True if a is greater than b
        self.assertGreaterEqual(100,10) ## True if a is greater or equal to b
        self.assertLess(10,100)        ## True if a is less than b
        self.assertLessEqual(10,100)   ## True if a is less os equal to b
        self.assertEqual(100,100)  ## True if a is equal to b

if __name__=="__main__":
    unittest.main()

