from datetime import datetime


class ShoppingCart:
    def __init__(self, user):
        self.__user = user
        self.__items = {}
        self.__created_at = datetime.now()
        self.__total = 0.0

    def add_item(self, book, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            if quantity > book.quantity:
                raise ValueError(
                    f"Sorry, only {book.quantity} copies available"
                )

            if book in self.__items:
                new_quantity = self.__items[book] + quantity
                if new_quantity > book.quantity:
                    raise ValueError(
                        f"Sorry, only {book.quantity} copies available"
                    )
                self.__items[book] = new_quantity
            else:
                self.__items[book] = quantity

            self.__update_total()
            return True
        except ValueError as e:
            print(f"\nError: {e}")
            return False

    def remove_item(self, book, quantity):
        try:
            if book not in self.__items:
                raise ValueError("Item not in cart!")

            if quantity <= 0:
                raise ValueError("Quantity must be positive!")

            if quantity > self.__items[book]:
                raise ValueError(
                    f"Can only remove up to {self.__items[book]} items!"
                )

            if self.__items[book] <= quantity:
                del self.__items[book]
                book.quantity += quantity
            else:
                self.__items[book] -= quantity
                book.quantity += quantity

            self.__update_total()
            return True
        except ValueError as e:
            print(f"\nError: {e}")
            return False

    def clear_cart(self):
        self.__items.clear()
        self.__total = 0.0

    def get_items(self):
        return self.__items

    def get_total(self):
        return self.__total

    def __update_total(self):
        self.__total = sum(
            book.price * quantity for book, quantity in self.__items.items()
        )
