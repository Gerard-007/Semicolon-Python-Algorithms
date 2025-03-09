class Book:
    def __init__(self, title, author, isbn, price, quantity):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__price = price
        self.__quantity = quantity

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        if not self.__isbn.isdigit():
            raise ValueError("ISBN must be an integer")
        self.__isbn = isbn

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = value

    def __str__(self):
        return f"{self.__title} by {self.__author} - ${self.__price:.2f} (ISBN: {self.__isbn}, Stock: {self.__quantity})"
