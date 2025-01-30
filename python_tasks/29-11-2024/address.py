class Address:
    def __init__(self, number: int, street: str, city: str, state: str):
        self.__number = number
        self.__street = street
        self.__city = city
        self.__state = state

    def __str__(self):
        return f"{self.__number}\n{self.__street}\n{self.__city}\n{self.__state}"