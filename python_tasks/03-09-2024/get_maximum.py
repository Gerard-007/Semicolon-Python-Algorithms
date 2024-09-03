def get_maximum_number(first, second, third):
	max_number = first
	if max_number < second:
		max_number = second
	elif max_number < third:
		max_number = third
	return max_number


maximum_number = get_maximum_number(30, 42, 52)

print(f"The maximum number is {maximum_number}")