def multiply_numbers(num1, num2):
    total = 0

    if num1 == 0 or num2 == 0:
        return 0

    if num2 < 0:
        return -multiply_numbers(num1, -num2)

    for _ in range(num2):
        total += num1
    return total

print(multiply_numbers(2, -2))