# Task 4
def left_right_triangle(number):
    counter = number
    for i in range(1, number+1):
        print(' ' * counter, end="")
        for j in range(i, 0, -1):
            print(f"{j if j % 2 != 0 else '*'}", end="")
        counter -= 1
        print()

    for i in range(1, number+1):
        print(' ' * number, end="")
        for k in range(1, i+1):
            print(k if k % 2 != 0 else "*", end="")
        print()

left_right_triangle(10)