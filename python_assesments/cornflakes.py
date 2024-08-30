"""
1 - Create a function called <corn_flakes()> with a parameter called <number>
2 - Inside the <corn_flakes()> generate a <for loop> with range of 1 to 10
3 - Multiply the parameter <number> with the values from the range 1 to 10
4 - Generate an option menu using <while loop> set the condition as True
5 - Request an input from user and represent the value as <options>
6 - Using <match case> check if user entered zero then exit the program
7 - If user entered "1" then request an input to multiply till 10
8 - Represent the value as <number_input>
9 - Call the <corn_flakes()> function and enter the <number_input> as argument of the function
10 - Wrap the task 8 and 9 with a <try/exception> block.
"""


def corn_flakes(number):
	for num in range(1, 11):
		print(f"{number} x {num} = {number * num}")


while True:
	options = input("Enter 1 to start or 0 to exit: ")
	match options:
		case "0":
			print("Exiting Program...")
			break
		case "1":
			try:
				number_input = int(input("Enter a number: "))
				corn_flakes(number_input)
			except Exception as e:
				print(f"Bia oga! enter a number!, {e}")