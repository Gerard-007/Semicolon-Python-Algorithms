def largest_item(array):
    largest = array[0]
    for index in array:
        if largest < index:
            largest = index
    return largest


def reverse_array(array):
    return array[::-1]


def element_occurance(num, array):
    return f"{num} already exists in the arrat" if num in array else "Number doesnt exists"


def odd_elements(array):
    result = []
    for index in range(len(array)):
        if index % 2 != 0:
            result.append(array[index])
    return result


def even_elements(array):
    result = []
    for index in range(len(array)):
        if index % 2 == 0:
            result.append(array[index])
    return result


def running_total(array):
    total = 0
    for element in array:
        total += element
    return total


def is_palindrome(data):
    return "Is Palindrome "if isinstance(data, str) and data == data[::-1] else "Not a palindrome"


def compute_with_forloop(array):
    sum_array = 0
    for index in array:
        sum_array += index if isinstance(index, int, float) else 0
    return sum_array


def compute_with_whileloop(array):
    sum_array = 0
    counter = 0
    while counter < len(array):
        sum_array += array[counter] if isinstance(array[counter], int, float) else 0
        counter += 1
    return sum_array



array = [2, 4, 5, 6, 3]
print(f"Largest element: {largest_item(array)}")
print(f"Reversed list: {reverse_array(array)}")
num = int(input("Enter a number to check: "))
print(f"Check number in list: {element_occurance(num, array)}")
print(f"Odd elements: {odd_elements(array)}")
print(f"Even elements: {even_elements(array)}")
print(f"Running total: {running_total(array)}")
data = str(input("Enter a data to check for palindrome: "))
print(f"Palindrome: {is_palindrome(data)}")
