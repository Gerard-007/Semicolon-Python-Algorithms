import random
from enum import property


class User:
    users = []

    def __init__(self, first_name, last_name, email, phone, gender):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__gender = gender
        self.__username = None
        self.generate_username()
        self.users.append(self)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not value.isdigit() or len(value) != 11:
            raise ValueError("Phone must be 11 digits")
        self.__phone = value

    def get_phone(self):
        return self.__phone

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_username(self):
        return self.__username

    def generate_username(self):
        username = self.__email.split("@")[0]
        temp_username = username
        username_exists = any(
            user.get_username() == temp_username for user in self.users
        )
        if username_exists:
            temp_username = f"{username}{random.randint(1000, 9999)}"
        self.__username = temp_username

    def __str__(self):
        return f"""
            Name: {self.__first_name} {self.__last_name}
            Username: {self.__username}
            Email: {self.__email}
            Phone: {self.__phone}
            Gender: {self.__gender}
        """
