import unittest

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print("setup for testcase")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self): 
        print("teardown for testcase")

if __name__ == '__main__':
    unittest.main(verbosity=2)