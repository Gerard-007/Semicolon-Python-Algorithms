"""
    create a function that implements a simple ROT13 cipher
    the function should take a string as input and return a new
    string with each character shifted by 13 positions in the
    alphabet, wrapping around if necessary. Non-alphabetic character
    should be left unchanged.
    
    sample input: "Hello World"
    Sample output: "Uryyb Jbeyq"
"""

import string


def encryption_method(text):
    uppercase_list = string.ascii_uppercase
    lowercase_list = string.ascii_lowercase
    for char in text:
        if not char.isalpha():
            continue
        if char.isupper():
            if char in uppercase_list:
                index = uppercase_list[uppercase_list.index(char)+1:]
                print(index, "\n")
        elif char.islower():
            if char in lowercase_list:
                index = lowercase_list[lowercase_list.index(char)+1:]
                print(index, "\n")

encryption_method("Test")
    

def decryption_method(text):
    ...