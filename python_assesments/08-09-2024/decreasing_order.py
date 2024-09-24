
display_sorted_numbers(num1, num2, num3):
	lowest_num = 0
	if num1 > num2:
		lowest_num = num1
		num1 = num2
		num2 = lowest_num
	if num1 > num3:
		lowest_num = num1
		num1 = num2
		num2 = lowest_num
	if num2 > num3:
		lowest_num = num2
		num2 = num3
		num3 = lowest_num
	print(f"{float(num1)} {float(num2)} {float(num3)}")


display_sorted_numbers(23, 13, 21)
	