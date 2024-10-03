def check_for_negative_number(user_input):
    if user_input > 3000 or user_input < 1000 or isinstance(user_input, str):
        return "Invalid input must be a number between 1000 - 3000"
    result = []
    for i in str(user_input):
        if int(i) % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return False if False in result else True


user_input = int(input("Enter a digit from 1000 to 3000: "))
print(check_for_negative_number(user_input))