from decimal import Decimal
from account import Account

class Bank:
    def __init__(self, name) -> None:
        self._name: str = name
        self.accounts: list = []

    def register_account(self, name, phone, pin) -> Account:
        account: Account = Account(name, phone, pin)
        self.accounts.append(account)
        return account

    def get_account(self, account_number: str) -> Account:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        # sourcery skip: raise-specific-error
        raise Exception("Account not found")

    def deposit(self, account_number: str, amount: Decimal) -> None:
        self.get_account(account_number).deposit(amount)

    def withdraw(self, account_number: str, amount: Decimal, pin:str) -> None:
        self.get_account(account_number).withdraw(amount, pin)

    def transfer(self, sender:Account, recipient:Account, amount: Decimal, pin: str) -> None:
        sender_account = self.get_account(sender)
        recipient_account = self.get_account(recipient)
        sender_account.withdraw(amount, pin)
        recipient_account.deposit(amount)
