def compute_string_numbers(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))


result = compute_string_numbers("20", "12")


print(f"result: {result}")
print(f"type: {type(result)}")
