def palindrome_prime_number(num):
    if num % 2 == 0 and str(num) == str(num)[::-1]:
        return True
    return False