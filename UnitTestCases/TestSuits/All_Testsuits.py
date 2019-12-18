import unittest
from UnitTestCases.Package1.TC_Login import loginTest
from UnitTestCases.Package1.TC_Signup import SignupTest
from UnitTestCases.Package2.TC_Payment import PaymentTest
from UnitTestCases.Package2.TC_PaymentReturn import PaymentReturn

tc1=unittest.TestLoader().loadTestsFromTestCase(loginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

sanitytestsuit=unittest.TestSuite([tc1,tc2])
mastertestsuit=unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner().run(mastertestsuit)