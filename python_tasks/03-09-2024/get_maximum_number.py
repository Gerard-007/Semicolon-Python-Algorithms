def get_maximum_number(first_number, second_number, third_number):
	max_number = first_number
	if max_number < second_number:
		max_number = second_number
	elif max_number < third_number:
		max_number = third_number
	return max_number


def get_minimum_number(first_number, second_number, third_number):
	min_number = first_number
	if min_number > second_number:
		min_number = second_number
	elif min_number > third_number:
		min_number = third_number
	return min_number 


maximum_number = get_maximum_number(100, 81, 72)
print(f"The maximum number is {maximum_number}\n")


minimum_number = get_minimum_number(30, 42, 72)
print(f"The minimum number is {minimum_number}")