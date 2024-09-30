def multiply_numbers(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        total = 0
        if num1 == 0 or num2 == 0:
            return 0

        if num1 < 0:
            return -multiply_numbers(-num1, num2)
        elif num2 < 0:
            return -multiply_numbers(num1, -num2)
        elif num1 < 0 and num2 < 0:
            return multiply_numbers(-num1, -num2)

        for _ in range(num2):
            total += num1
        return total
    return "Invalid input type must be of int type"

print(multiply_numbers(-2, -2))
print(multiply_numbers(2, -2))
print(multiply_numbers(-2, 2))