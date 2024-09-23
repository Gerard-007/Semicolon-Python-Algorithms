"""
- Declare a new list and represent it as <new_list>
- Using while loop request an number input from user to be added to <new_list>
- Represent the values as <list_element>
- While <list_element> is 0 stop the loop
- Append <list_element> to <new_list>
- Display <new_list>
"""

new_list = []

while True:
	try:
		list_element = int(input("Enter 0 to exit or keep entering a number to add into the list: "))
	except Exception as e:
		print(f"Invalid input must be a number or 0 to exit! {e}")
	else:
		if list_element == 0:
			print("Exiting...")
			break
		new_list += [list_element]

print(new_list)


"""
- Declare a variable <sum_list>
- Loop through the items in <new_list>
- For each item sum them to <sum_list>
- Divide the <sum_list> by the length of <new_list>
- Display the output.
- Wrap the code into a function called <sum_list()> that accepts list as parameter
"""

def sum_list(new_list):
	sum_list = 0
	for index in range(len(new_list)):
		sum_list += new_list[index]
	print(f"Average: {sum_list / len(new_list)}")


sum_list(new_list)
	
