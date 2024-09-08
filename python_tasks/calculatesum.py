number = 666

if number >= 1 and number <= 999:
	str_number = f"{number}"
	reversed_number = ""
	sum_numbers = 0
	if str_number[::-1] == str_number:
		print(f"1 - reversed str_number = {str_number[::-1]}")
		for sn in str_number:
			if int(sn) % 2 == 0:
				reversed_number += sn
				if reversed_number  == str_number:
					for sn in str_number:
						sum_numbers += int(sn)
			else:
				print("Odd palindrum number...")
	print(f"4 - The total number is {sum_numbers }")
else:
	print("Guy kinin problem!")