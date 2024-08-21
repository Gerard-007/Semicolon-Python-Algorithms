'''
    1 - Request a number input from user for three times 
    2 - Store the three input values as input1, input2, input3
    3 - Sum the three inputs and divine by 3
    4 - Represent the result as average
    5 - Display average
'''

try:
	input1 = int(input("Enter the first number: "))
	input2 = int(input("Enter the second number: "))
	input3 = int(input("Enter the third number: "))

	average = (input1 + input2 + input3)/3

	print(f"The average is: {average}")
except Exception as e:
	print(f"Exception: {e}")
	print(f"You didnt enter a number in some of the inpus please enter a number!")