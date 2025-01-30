class Account:
    def __init__(self) -> None:
        self._balance = 0

    def validate_amount(self, amount: float) -> None:
        if amount is None:
            raise ValueError("Amount is required")
        elif not isinstance(amount, (float, int)):
            raise TypeError("Invalid amount type")
        elif amount < 0:
            raise ValueError("Amount must be greater than zero")

    def get_balance(self) -> int:
        return self._balance

    def deposit(self, amount: float) -> None:
        self.validate_amount(amount)
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self.validate_amount(amount)
        if amount > self._balance:
            raise ValueError("You have low balance")
        self._balance -= amount

