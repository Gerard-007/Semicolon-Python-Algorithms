def multiple_table(a_start, b_start, count):
    print("a  b  a**b")
    counter = 0
    while counter <= count-1:
        print(f"{a_start + counter}  {b_start + counter}  {(a_start + counter) ** (b_start + counter)}")
        counter += 1
    
multiple_table(1, 2, 5)