import unittest
from converter import converter


class TestConverter(unittest.TestCase):

    def test_that_converter_function_exists(self):
        converter(100)

    def test_that_converter_function_return_correct_value(self):
        amount = 100
        result = 1550 * amount
        self.assertEqual(converter(amount), result)

    def test_that_converter_function_checks_for_negative_value(self):
        self.assertRaises(ValueError, converter, -1)

    # def test_that_converter_function_checks_for_wrong_value_type(self):
    #     self.assertRaises(TypeError, converter, "byte")

    def test_that_converter_function_checks_for_wrong_value_type(self):
        self.assertEqual(converter("byte"), "invalid input")
        self.assertEqual(converter(""), "invalid input")