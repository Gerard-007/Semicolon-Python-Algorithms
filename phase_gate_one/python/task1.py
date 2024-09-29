import random


random_number_1 = random.randint(1, 100)
random_number_2 = random.randint(1, 100)

def sum_of_numbers(number_input):
    if number_input == (random_number_1 + random_number_2):
        return True
    return False



user_input = int(input(f"What is the sum of {random_number_1} and {random_number_2}: "))
print(sum_of_numbers(number))
