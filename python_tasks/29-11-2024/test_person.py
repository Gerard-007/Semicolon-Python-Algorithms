import unittest
from person import Person


class TestPerson(unittest.TestCase):
    person: Person = Person("Gerard", 100)

    def test_that_person_class_exists(self):
        self.assertTrue(self.person)

    def test_that_person_age_cannot_be_less_than_zero(self):
        self.assertRaises(ValueError, self.person.set_age, -100)
