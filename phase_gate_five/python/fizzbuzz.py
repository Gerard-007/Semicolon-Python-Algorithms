def fizzbuzz(number):
    result = {}
    if number > 50 or number < 1:
        return "Invalid input ranges from 1 - 50"
    for num in range(1, number+1):
        if num % 3 == 0 and num % 5 == 0:
            result[num] = "FizzBuzz!"
        elif num % 3 == 0:
            result[num] = "Fizz!"
        elif num % 5 == 0:
            result[num] = "Buzz!"
    return result


for k, v in fizzbuzz(50).items():
    print(f"{k}: {v}")