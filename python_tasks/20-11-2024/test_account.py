import unittest
from account import Account


class TestAccount(unittest.TestCase):
    account : Account = Account()

    def test_that_balance_and_withdrawal_works(self):
        #Check
        self.assertEqual(self.account.get_balance(), 0)

        #When
        self.account.deposit(500)
        #Check
        self.assertEqual(self.account.get_balance(), 500)

        #When
        self.account.withdraw(100)
        #Check
        self.assertEqual(self.account.get_balance(), 400)

    def test_that_deposit_and_withdrawal_does_not_take_negative_amount(self):
        self.assertRaises(ValueError, self.account.deposit, -400)
        self.assertRaises(ValueError, self.account.withdraw, -400)

    def test_that_withdrawal_is_not_more_than_balance(self):
        self.account.deposit(2000)
        self.assertRaises(ValueError, self.account.withdraw, 5000)

    def test_for_amount_type_input(self):
        self.assertRaises(TypeError, self.account.deposit, "5000")
        self.assertRaises(TypeError, self.account.withdraw, "-3000")