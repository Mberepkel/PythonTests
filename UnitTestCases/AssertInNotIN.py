import unittest
class Test(unittest.TestCase):
    def test_case(self):
        list= ("python","Selenium","java")
        self.assertIn("python",list)
        for items in list:
            print (items)
        self.assertNotIn("Selenium",list)

if __name__ == "__main__":
    unittest.main()






