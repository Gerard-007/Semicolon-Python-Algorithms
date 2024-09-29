def sort_generated_list():
    result = []
    for num in range(3):
        user_input = int(input(f"Enter number ({num + 1}): "))
        result.append(user_input)
        result.sort()
    return result
   
get_sorted_list = sort_generated_list()
print(get_sorted_list)
