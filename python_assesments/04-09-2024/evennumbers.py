

def get_even_numbers(number):
    for num in range(0, number + 1, 2):
        if num % 2 == 0:
            print(num, " ", end="")

get_even_numbers(100)