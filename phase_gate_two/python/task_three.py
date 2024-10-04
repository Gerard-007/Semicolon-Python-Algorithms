def custom_list_functions(number_list):
    length_counter = 0
    sum_even_position = 0
    sum_odd_position = 0
    multiply_third_position = 1
    sum_of_average = 0
    for num in number_list:
        length_counter += 1
        
        if length_counter % 2 != 0:
            sum_odd_position += num

        if length_counter % 2 == 0:
            sum_even_position += num

        if length_counter % 3 == 0:
            multiply_third_position *= num

        sum_of_average += num
    total_average = sum_of_average/length_counter

    print(f"""
    Length of list: {length_counter}
    Sum of elements in even positions: {sum_even_position}
    Sum of elements in odd positions: {sum_odd_position}
    Multiples elements at every third positions: {multiply_third_position}
    Total average of all elements in the list: {total_average}
    """)
    
 
number_list = []


while True:
    if len(number_list) != 10:
        user_input = int(input("Enter a number ranging from 1 to 50: "))
        if user_input > 50 or user_input < 1 or isinstance(user_input, str):
            print("Invalid input you must enter from 1 to 50!")
            continue
        number_list.append(user_input)
    break


custom_list_functions(number_list)