# Task 3
def febunashi(given_number):
    fnumber1 = 0
    fnumber2 = 1
    next_fnumber = fnumber2  
    counter = 0

    for _ in range(1, given_number+1):
        if counter == given_number:
            break
        fnumber1 = fnumber2
        fnumber2 = next_fnumber
        next_fnumber = fnumber1 + fnumber2
        print(next_fnumber, end=" ")
        counter += 1

febunashi(20)