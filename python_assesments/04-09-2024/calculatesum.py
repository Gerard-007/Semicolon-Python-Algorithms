

def calculate_multiples_of_10(number):
    sum_multiple = 0
    for num in range(1, number + 1):
        if num % 10 == 0:
            sum_multiple += num
    print(f"Total: {sum_multiple}")


calculate_multiples_of_10(20000)