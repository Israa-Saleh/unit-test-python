import unittest
from calculator import *


class TestCaculator(unittest.TestCase):

    def test_sum(self):
        testObj = Calculator()
        self.assertEqual(testObj.add(2,3), 2+3)

    def test_sub(self):
        testObj = Calculator()
        self.assertEqual(testObj.subtract(2,3), 2-3)

    def test_multiply(self):
        testObj = Calculator()
        self.assertEqual(testObj.multiply(2,3), 2*3)

    def test_divide(self):
        testObj = Calculator()
        self.assertEqual(testObj.divide(2,3), 2/3)

    def test_maximum(self):
        testObj = Calculator()
        self.assertEqual(testObj.maximum(2, 3), max(2, 3))

    def test_minimum(self):
        testObj = Calculator()
        self.assertEqual(testObj.minimum(2, 3), min(2, 3))


if __name__ == '__main__':
    unittest.main()
