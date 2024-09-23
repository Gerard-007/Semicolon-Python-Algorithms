def converter(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Invalid type of amount")
    if amount <= 0:
        raise ValueError("Invalid amount")
    RATE = 1550
    return round(amount * RATE)

try:
    amount = float(input("Enter amount: "))
except ValueError as e:
    raise ValueError("Invalid amount") from e
except TypeError as e:
    raise TypeError("Invalid data type") from e
except Exception as e:
    print("I dont know what you want!.")