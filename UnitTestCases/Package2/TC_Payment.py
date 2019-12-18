import unittest
class  PaymentTest(unittest.TestCase):

    def test_paymentbyeuro(self):
        print("this is payment by euro test")
        self.assertTrue(True)
    def test_paymentbypounds(self):
        print("this is login by pounds test")
        self.assertTrue(True)
    def test_paymentbydollar(self):
        print("this is payment by dollar test")
        self.assertTrue(True)

if __name__== "__main__":
    unittest.main()