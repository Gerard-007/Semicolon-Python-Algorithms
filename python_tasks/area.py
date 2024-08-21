'''
    1 - Create a variable called radius 
    2 - Initialize the variable radius with value 10
    3 - Compute by multiplying radius with radius and 3.142
    4 - Represent the result as area
    5 - Display area
'''

# radius = 10
try:
	radius = int(input("Enter radius: "))
	area = 3.142 * (radius ** 2)
	print(f"Pi radius: {area}")
except Exception as e:
	print(f"Exception: {e}")
	print(f"You didnt enter a number please enter a number!")