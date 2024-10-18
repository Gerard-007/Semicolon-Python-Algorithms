def get_multiple_array(row, col):
	for i in range(1, col+1):
		for j in range(1, row+1):
			print(f"{i*j:2}", end=" ")
		print()


try:
	rows = int(input("Enter number of rows: "))
	cols = int(input("Enter number of columns: "))
except Exception as e:
	print("Please enter a number!")
else:
	get_multiple_array(rows, cols)