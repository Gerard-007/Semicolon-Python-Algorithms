def binary_search(list, item):
    '''
        Low and High keep track of which 
        part of the list you will search in.
    '''
    low = 0
    high = len(list) - 1

    '''
    While you haven’t narrowed it down
    to one element
    '''
    while low <= high:
        mid = (low + high) // 2 # check the middle element.
        guess = list[mid]
        if guess == item: # Found the item.
            return mid
        if guess > item: # Guess was too high
            high = mid - 1
        else: # Guess was too high
            low = mid + 1
    return None # Item doesnt exist

my_list = [1, 3, 5, 7, 9] # Lets test it
print(binary_search(my_list, 3)) # => 1

        