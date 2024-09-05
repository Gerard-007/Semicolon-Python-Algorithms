def reverse_triangle(number):
	for x in range(number, 0, -1):
		for y in range(x, 0, -1):
			print(y, " ", end="")
		print()


reverse_triangle(20)