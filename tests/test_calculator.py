import unittest

import src.calculator as cal
# from src.calculator import sum, substract, multiply

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert cal.sum(2,3) == 5

    def test_substract(self):
        assert cal.substract(10,5) == 5

    def test_multiply(self):
        assert cal.multiply(2,5) == 10

    def test_divide(self):
        assert cal.divide(10,2) == 5

    def test_divide_fail_zeroDivision(self):
        with self.assertRaises(ValueError):
            cal.divide(10,0)