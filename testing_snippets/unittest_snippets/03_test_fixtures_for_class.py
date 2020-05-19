import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup for class")

    def setUp(self):
        print("setup for test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("teardown for test")

    @classmethod
    def tearDownClass(cls):
        print("teardown for class")


if __name__ == '__main__':
    unittest.main(verbosity=2)