import unittest
from task6 import multiply_numbers


class TestMultiplication(unittest.TestCase):

    def test_that_nultiplication_function_exists(self):
         multiply_numbers(2, 3)

    def test_that_multiplication_function_return_correct_value(self):
        a = 10
        b = 2
        self.assertEqual(multiply_numbers(a, b), 20)

    def test_that_multiplication_function_can_multiply_negative_numbers(self):
        a = -10
        b = 2
        self.assertEqual(multiply_numbers(a, b), -20)

    def test_that_multiplication_function_can_multiply_negative_numbers(self):
        a = 10
        b = -2
        self.assertEqual(multiply_numbers(a, b), -20)

    def test_that_multiplication_function_can_multiply_negative_numbers(self):
        a = -10
        b = -2
        self.assertEqual(multiply_numbers(a, b), 20)

    # def test_that_multiplication_function_checks_for_zero_value(self):
    #     self.assertRaises(ValueError, converter, -1)