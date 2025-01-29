from decimal import Decimal
from account_utility import validate_amount


class Account:
    def __init__(self, name:str, phone:str, pin:str) -> None:
        self._name = name
        self.phone = None
        self.set_phone(phone)
        self.__pin = None
        self.set_pin(pin)
        self._balance = Decimal(0.00)
        self.account_number = self.generate_account_number(phone)

    def get_name(self):
        return self._name

    def get_phone(self):
        return self.phone

    def get_balance(self) -> Decimal:
        return self._balance

    def set_phone(self, phone: str) -> None:
        if len(phone) != 11:
            raise ValueError("Phone number must be of length 11 numbers")
        self.phone = phone

    def set_pin(self, pin: str) -> None:
        if len(pin) != 4:
            raise ValueError("Pin must be 4 digits")
        self.__pin = pin.strip()

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        if self.__pin == old_pin.strip():
            self.set_pin(new_pin)
        raise ValueError("Old pin didn't match!")

    def generate_account_number(self, phone: str) -> str:
        if phone is not None:
            return phone[1:]
        else:
            raise ValueError("Phone number must be provided")

    def deposit(self, amount: Decimal) -> None:
        validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount: Decimal, pin: str) -> None:
        validate_amount(amount)
        if self.__pin != pin:
            raise ValueError("Incorrect transaction pin")
        if amount > self._balance:
            raise ValueError("You have low balance")
        self._balance -= amount

    def __str__(self) -> str:
        return f"""
            Name: {self._name.title()}
            Phone: {self.get_phone()}
            Account: {self.account_number}
            Balance: ₦{self._balance}
            Pin: {self.__pin}
        """
