from address import Address

class Person():
    def __init__(self, name: str, age: int, dob: str, phone: str, gender: str, number: int, street: str, city: str, state: str):
        self.__name = name
        self.__age = age
        self.__dob = dob
        self.__phone = phone
        self.__gender = gender
        self.__address = Address(number, street, city, state)

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age <= 0 or age is None:
            raise ValueError("Number of age must be greater than zero.")
        else:
            self.__age = age

    def set_name(self, name):
        self.__name = name
