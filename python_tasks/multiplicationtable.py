def get_multiplication_table(number):
	for i in range(1, number+1):
		fro j in range(1, 13):
			print(f"{i:>2} * {j:<2} = {i * j:<4}", end="")
		print()