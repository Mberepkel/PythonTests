import unittest

class loginTest(unittest.TestCase):

    def test_loginbyEmail(self):
        print("this is login email test")
        self.assertTrue(True)

    def test_loginbyfacebook(self):
        print("this is login by facebook test")
        self.assertTrue(True)

    def test_loginbyTwiter(self):
        print("this is login by Twiter test")
        self.assertTrue(True)


if __name__== "__main__":
    unittest.main()