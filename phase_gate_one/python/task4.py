def sum_digits(user_input):
    sum_digits = 0
    if user_input <= 0 or user_input > 1000:
        print("Invalid input should be 1 - 1000")
    else:
        for num in str(user_input):
            sum_digits += int(num)
    return sum_digits


user_input = int(input("Enter a number between 1 - 1000: "))
print(sum_digits(user_input))