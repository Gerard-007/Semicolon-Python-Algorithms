import unittest
import cube

class TestCube(unittest.TestCase):
	def test_that_cube_function_exist(self):
		cube.get_cube(3)

	def test_that_cube_function_returns_result(self):
		self.assertEqual(cube.get_cube(10), 1000)
		self.assertEqual(cube.get_cube(7),  343)

	def test_that_cube_function_raises_error_with_negative_amount(self):
		self.assertRaises(ValueError, cube.get_cube, -3)

	def test_that_cube_function_raises_error_with_string_value(self):
		self.assertRaises(TypeError, cube.get_cube, "byte")