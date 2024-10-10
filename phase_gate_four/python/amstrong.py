def amstrong(number):
    result = 0
    for i in str(number):
        cube = int(i)**3
        result += cube
    print(f"Result: {result}")
    

amstrong(153)