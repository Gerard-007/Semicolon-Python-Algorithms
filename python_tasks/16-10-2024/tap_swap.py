def swap(array: list) -> list:
    result = []
    for index in range(0, len(array)-1 if len(array) % 2 != 0 else len(array) , 2):
        temp = array[index]
        array[index] = array[index + 1]
        array[index + 1] = temp
        result.append(array[index])
        result.append(array[index + 1])
    result.append(array[-1]) if len(array) % 2 != 0 else result
    return result