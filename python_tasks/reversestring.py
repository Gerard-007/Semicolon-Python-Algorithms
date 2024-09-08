'''
- get string from user and represent it as <user_input>.
- convert <user_input> to list and represent it as <user_input_list>.
- looping through <user_input> use pop() function to get the last item in <user_input_list> list.
- represent the result as <result>.
- Display the result...
'''

'''
def reverse_string(user_input):
	user_input_list = list(user_input)
	for rev in user_input:
		result = user_input_list.pop()
		print(result, end="")


reverse_string("MummyWa") 
'''


def reverse_word(word):
	reversed_word = ""
	for num in range(len(word) - 1, -1, -1):
		reversed_word += word[number]
	return reversed_word