import unittest
from bank import Bank


class TestBank(unittest.TestCase):
    bank = Bank("Genas Bank")


    def test_for_account_creation(self):
        self.bank.register_account(
            "Gerard",
            "08062134747",
            "0123",
        )
        self.assertEqual(len(self.bank.accounts), 1)

    def test_that_user_can_deposit(self):
        self.bank.register_account(
            "Gerard",
            "08062134747",
            "0123",
        )
        self.bank.deposit("8062134747", 2000)
        current_account = self.bank.get_account("8062134747")
        self.assertEqual(current_account.__balance, 2000)

    def test_that_user_can_withdraw(self):
        ...

    def test_that_user_can_transfer(self):
        ...
