from datetime import datetime

class ShoppingCart:
    def __init__(self, user):
        self.__user = user
        self.__items = {}
        self.__created_at = datetime.now()
        self.__total = 0.0

    def add_item(self, book, quantity=1):
        if book in self.__items:
            self.__items[book] += quantity
        else:
            self.__items[book] = quantity
        self.__update_total()

    def remove_item(self, book, quantity=1):
        if book in self.__items:
            if self.__items[book] <= quantity:
                del self.__items[book]
            else:
                self.__items[book] -= quantity
            self.__update_total()

    def clear_cart(self):
        self.__items.clear()
        self.__total = 0.0

    def get_items(self):
        return self.__items

    def get_total(self):
        return self.__total

    def __update_total(self):
        self.__total = sum(book.get_price() * quantity for book, quantity in self.__items.items())
