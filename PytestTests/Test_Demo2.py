import pytest

@pytest.yield_fixture()
def setup():
    print ("once before every method")
    yield
    print ("once after every method")

def testMethod1(setup) :
    print("this is test method1")

def testMethod2(setup) :
    print("this is test method2")

def testMethod3(setup) :
    print("this is test method3")

## to run a test case in a file take directory of the file and add ::testcase, eg pytest -v -s PytestTests/Test_Demo2.py::testMethod2

