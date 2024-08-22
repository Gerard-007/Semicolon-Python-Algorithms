'''
    - Prompt user to enter their password
    - Represent their input <password>
    - Compute the length of the <password> using len() function
    - Represent the length of the <password> as <password_length>
    - Miltiply "*" with <password_length>
    - Represent the result as <hashed_password> 
    - Display the <hashed_password>
'''

password = input("Enter password: ")
password_length = len(password)
hashed_password = "*" * password_length
print(hashed_password)