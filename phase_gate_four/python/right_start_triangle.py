# Task 1
def right_start_triangle(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(j if j % 2 != 0 else "*", end=" ")
        print()

right_start_triangle(5)
