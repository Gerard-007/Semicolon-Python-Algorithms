import string
import random



def password_generator():
    password = []
    password.extend(random.choices(string.ascii_lowercase, k=4)) 
    password.extend(random.choices(string.ascii_uppercase, k=4))
    password.extend(random.choices(string.punctuation, k=4))
    password.extend(random.choices(string.digits, k=4))
    return str("".join(password))


def password_validator(password):
    if not any(pwd for pwd in password if pwd in string.ascii_lowercase):
        return "Password must include lower cased letters."
    elif not any(pwd for pwd in password if pwd in string.ascii_uppercase):
        return "Password must include upper cased letters."
    elif not any(pwd for pwd in password if pwd in string.digits):
        return "Password must include numeric values."
    elif not any(pwd for pwd in password if pwd in string.punctuation):
        return "No character found! your password must contain a character."
    elif len(password) < 16:
        return "Invalid password length! password must be 16 in character."
    else:
        return "Password is valid!"


password = password_generator()
print(f"Password: {password}")
print(password_validator(password))