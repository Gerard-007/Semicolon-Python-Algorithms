from decimal import Decimal


def validate_balance(instance, amount: Decimal) -> Decimal:
    if amount < Decimal('0.0'):
        raise ValueError("Invalid balance amount")
    instance.balance = amount
    return instance.balance

def generate_account_number(instance) -> str:
    print(instance.phone)
    if instance.phone is not None:
        return instance.phone[1:]
    else:
        raise ValueError("Phone number must be provided")

def validate_phone_number(value) -> bool:
    return len(value) == 11

def validate_amount(amount: Decimal) -> None:
    if amount is None:
        raise ValueError("Amount is required")
    elif amount < Decimal('0.0'):
        raise ValueError("Amount must be greater than zero")
