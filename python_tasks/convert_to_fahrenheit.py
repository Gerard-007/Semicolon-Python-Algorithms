"""
    - Request an input from user and store it as <celsius>
    - Calculate the fahrenheit using this formulae <(9/5) * celsius + 32>
    - Represent the result as <fahrenheit>
    - Wrap the above codes in a function
"""


def convert_to_fahrenheit(celsius):
    try:
        fahrenheit = (9/5) * celsius + 32
        print(f"fahrenheit: {fahrenheit}")
    except Exception as e:
        print("This is a test")


celsius = float(input("Enter celsius: "))
convert_to_fahrenheit(celsius)
