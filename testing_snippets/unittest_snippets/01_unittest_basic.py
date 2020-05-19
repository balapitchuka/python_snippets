import unittest

class TestCaseDemo(unittest.TestCase):


    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")


if __name__ == '__main__':
    unittest.main(verbosity=2)