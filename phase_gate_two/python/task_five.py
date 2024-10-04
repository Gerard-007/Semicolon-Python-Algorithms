def divide_or_square(number):
    if number <= 0:
        return 0
    if number % 5 == 0:
        return round(number ** (1/2), 2)
    return number % 5


print(divide_or_square(10))