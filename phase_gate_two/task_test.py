import unittest
from task_four import compute_string_numbers
from task_five import divide_or_square


class TaskFour(unittest.TestCase):

    def test_that_compute_string_numbers_function_exists(self):
         compute_string_numbers("2", "3")

    def test_that_compute_string_numbers_function_return_correct_value(self):
        a = "10"
        b = "10"
        self.assertEqual(compute_string_numbers(a, b), "20")

    def test_that_compute_string_numbers_function_can_compute_negative_numbers(self):
        a = "-10"
        b = "2"
        self.assertEqual(compute_string_numbers(a, b), "-8")

    def test_that_compute_string_numbers_function_can_compute_negative_numbers(self):
        a = "10"
        b = "-2"
        self.assertEqual(compute_string_numbers(a, b), "8")

    def test_that_compute_string_numbers_function_can_compute_two_negative_numbers(self):
        a = "-10"
        b = "-2"
        self.assertEqual(compute_string_numbers(a, b), "-12")


class TaskFive(unittest.TestCase):

    def test_that_divide_or_square_function_exists(self):
         divide_or_square(3)

    def test_that_divide_or_square_return_correct_value(self):
        x = 10
        self.assertEqual(divide_or_square(x), 3.16)

    def test_that_divide_or_square_function_returns_zero_with_negative_numbers(self):
        x = -10
        self.assertEqual(divide_or_square(x), 0)
