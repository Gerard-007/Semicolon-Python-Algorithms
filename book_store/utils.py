import datetime
import re


def display_main_option():
    print("""
    \n=== Welcome to Online Book Store ===
    1. Register
    2. Add Book
    0. Exit
    """)


def display_user_menu(bookstore):
    print(f"""
    \n=== Welcome {bookstore.current_user.get_first_name()} ===
    1. Browse Books
    2. Search Books
    3. View Shopping Cart
    4. Add Book to Cart
    5. Remove Book from Cart
    6. Place Order
    7. View Order History
    0. Exit
    """)


def validate_name(name):
    pattern = r"^[A-Za-z\s]+$"
    return bool(re.match(pattern, name))


def get_valid_name_input(prompt):
    while True:
        name = input(prompt).strip()
        if validate_name(name):
            return name
        print(
            "Error: Please enter only alphabets and no special characters or numbers."
        )


def validate_address(address):
    pattern = r"^[A-Za-z0-9\s]+$"
    return bool(re.match(pattern, address))


def get_valid_address_input(prompt):
    while True:
        address = input(prompt).strip()
        if validate_address(address):
            return address
        print(
            "Error: Please enter only letters and numbers eg . 123 Main St Anytown Nigeria"
        )


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt).strip()
        if validate_date(date_str):
            return date_str
        print("Error: Please enter date in YYYY-MM-DD format")


def validate_time(time_str):
    pattern = r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
    return bool(re.match(pattern, time_str))


def get_valid_time_input(prompt):
    while True:
        time_str = input(prompt).strip()
        if validate_time(time_str):
            return time_str
        print("Error: Please enter time in HH:MM format (24-hour)")


def validate_phone(phone):
    pattern = r"^\d{11}$"
    return bool(re.match(pattern, phone))


def get_valid_phone_input(prompt):
    while True:
        phone = input(prompt).strip()
        if validate_phone(phone):
            return phone
        print("Error: Please enter exactly 11 digits (e.g., 08012345678)")


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def get_valid_email_input(prompt):
    while True:
        email = input(prompt).strip()
        if validate_email(email):
            return email
        print(
            "Error: Please enter a valid email address (e.g., example@email.com)"
        )
