import math

def divide_or_square(num):
    if num % 5 == 0:
        return math.sqrt(num)
    return num % 5