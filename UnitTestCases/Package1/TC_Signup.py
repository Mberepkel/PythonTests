import unittest
class SignupTest(unittest.TestCase):

    def test_signupbyEmail(self):
        print("this is signup email test")
        self.assertTrue(True)

    def test_signupbyfacebook(self):
        print("this is signup by facebook test")
        self.assertTrue(True)

    def test_signupbyTwiter(self):
        print("this is signup by Twiter test")
        self.assertTrue(True)

if __name__== "__main__":
    unittest.main()