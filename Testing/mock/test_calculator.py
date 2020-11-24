from unittest import TestCase
from unittest.mock import patch
from .calculator import Calculator


class TestCalculator(TestCase):
    # def setUp(self):
    #     """Method called to prepare the test fixture. This is called immediately before calling the test method"""
    #     self.calc = Calculator()

    # call a mock sum function with well defined behavior, mock function always returns 9
    @patch("Testing.mock.calculator.Calculator.summary", return_value=9)
    def test_sum(self, summary):
        # answer = self.calc.summary(2, 4)
        self.assertEqual(summary(2, 3), 9)
