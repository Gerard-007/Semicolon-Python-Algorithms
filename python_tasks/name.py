'''
- Request an input from user
- Represent the value as <name>
- Check if <name> has a value 
- print the <name> if true else print "invalid name"
'''

name = input("Enter your name: ")

if name:
	print(f"Hello {name}")
else:
	print("Invalid name")