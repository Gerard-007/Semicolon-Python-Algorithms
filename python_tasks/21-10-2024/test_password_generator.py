import unittest
from password_generator import password_generator, password_validator


class TestPasswordValidator(unittest.TestCase):
    result = password_generator()

    def test_password_generator(self):
        self.assertEqual(len(self.result), 16)

    def test_for_valid_password(self):
        self.assertEqual(password_validator(self.result), "Password is valid!")

    def test_for_missing_lowercase(self):
        self.assertNotEqual(password_validator(self.result), "Password must include lower cased letters.")

    def test_for_missing_uppercase(self):
        self.assertNotEqual(password_validator(self.result), "Password must include upper cased letters.")

    def test_for_missing_digits(self):
        self.assertNotEqual(password_validator(self.result), "Password must include numeric values.")

    def test_for_missing_special_characters(self):
        self.assertNotEqual(password_validator(self.result), "No character found! your password must contain a character.")

    def test_for_short_password(self):
        self.assertNotEqual(password_validator("Gerard"), "Invalid password length! password must be 16 in character.")
