import unittest
from decimal import Decimal
from account import Account
from account_utility import validate_balance


class TestAccount(unittest.TestCase):
    account1 = Account("Gerard", "08062134747")

    def test_that_account_exists(self):
        self.account1._balance = Decimal("1000")

    def test_that_balance_cannot_be_negative(self):
        self.assertRaises(ValueError, validate_balance, self, Decimal("-1000.00"))

    def test_that_account_can_deposit_amount(self):
        self.account1.deposit(Decimal("2000"))
        self.assertEqual(self.account1._balance, Decimal("2000"))

    def test_that_account_cannot_deposit_negative_amount(self):
        self.assertRaises(ValueError, self.account1.deposit, Decimal("-1000.00"))
