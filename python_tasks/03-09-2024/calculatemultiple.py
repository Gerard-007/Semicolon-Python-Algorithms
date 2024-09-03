sum_multiples = 0

for number in range(1, 20001):
	if number % 10 == 0:
		sum_multiples += number
		print(f"{number} is divisible by 10")
print(f"The sum of multiples of 10 is {sum_multiples}")