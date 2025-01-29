def low_large(array: list) -> list:
    result = []
    large = array[0]
    low = array[0]
    for i in array:
        if large < i:
            large = i
        if low > i:
            low = i
    result.append(low)
    result.append(large)
    return result


array = [2, 3, 5, 6, 7]

print(low_large(array))