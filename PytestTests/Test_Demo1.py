import pytest

@pytest.fixture()
def setup():
    print ("one before every method")

def testMethod1(setup):
    print("this is test method1")

def testMethod2(setup):
    print("this is test method2")