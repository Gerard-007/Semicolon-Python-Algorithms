def ascending_order(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;
	print(array)



def descending_order(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] < array[j+1]:
				temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;
	print(array)



def multiply_third_elements(array):
	product = 1
	for i in range(len(array)):
		if i % 3 == 0:
			product *= array[i]
	print(product)



def square_of_elements(array):
	result = []
	for i in array:
		result.append(i**2)
	print(result)



array = [5, 2, 7, 1, 8, 2]



ascending_order(array)

descending_order(array)

multiply_third_elements(array)

square_of_elements(array)