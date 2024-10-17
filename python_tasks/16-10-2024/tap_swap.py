def swap(array: list) -> list:
    # if len(array) == 0 or len(array) % 2 != 0:
    #     raise Exception("Array length must be even and non-zero.")
    result = []
    for index in range(0, len(array), 2):
        temp = array[index]
        array[index] = array[index + 1]
        array[index + 1] = temp
        result.append(array[index])
        result.append(array[index + 1])
    
    return result