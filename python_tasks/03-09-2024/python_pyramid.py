"""
- Python Pyramid

"""

def build_pyramid(number):
	space = " "
	counter = number

	for x in range(1, number + 1):
		print(space * counter, "", end="")
	
		for y in range(x, 1, -1):
			print(y, end="")

		for z in range(1, x+1):
			print(z, end="")

		counter -= 1
		print()

build_pyramid(9)