def list_converter(array: list) -> list:
    result = [num**2 if num % 2 == 0 else num + 1 for num in array]
    return result

array = [5, 3, 8, 2, 5, 1, 0]

print(list_converter(array))