def reverse(number):
    return int(str(number)[::-1])


def is_palindrome(number):
    return "Is a palindrome." if reverse(number) == number else "Is not a palindrome."


print(is_palindrome(234))
print(is_palindrome(232))