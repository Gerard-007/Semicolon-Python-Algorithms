from typing import List


def permutate(a: int, b:int) -> float:
    pa = 1
    pb = 1
    for i in range(1, a+1):
        pa *= i
    for x in range(1, b+1):
        pb *= x
    return pa/(pa-pb)

print(permutate(5, 4))

