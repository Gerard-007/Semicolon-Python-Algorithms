'''
def gen_multi_array(number):
    multi_array = []
    child_array = []
    for _ in range(1, number+1):
        for _ in range(1, number+1):
            child_array.append(0)
        multi_array.append(child_array.copy())
        child_array.clear()
    return multi_array


multiple_array = gen_multi_array(10)


for element in range(len(multiple_array)):
    for item in multiple_array[element]:
        print(item, end=" ")
    print()
'''


# OR...


def get_multiple_array(row, col):
	two_dimensional_array = [[0] * row] * col
	for row in range(len(two_dimensional_array)):
    		for col in two_dimensional_array[row]:
        		print(col, end=" ")
    		print()

get_multiple_array(5, 10)