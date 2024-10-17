import unittest
import tap_swap

class TestTapSwap(unittest.TestCase):
	def test_that_tap_swap_function_exist(self):
		tap_swap.swap([])

	def test_that_tap_swap_function_returns_result(self):
		self.assertListEqual(tap_swap.swap([1, 2, 3, 4]), [2, 1, 4, 3])

	# def test_that_tap_swap_function_raises_error_with_array_length(self):
	# 	self.assertRaises(Exception, tap_swap.swap, [1, 2, 3])