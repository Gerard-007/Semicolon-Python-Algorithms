import os

from model.Book import Book
from model.Order import Order
from model.Payment import Payment, PaymentMethod
from model.ShoppingCart import ShoppingCart
from model.User import User
from utils import display_main_option, display_user_menu


class BookStore:
    def __init__(self):
        self.current_user = None
        self.shopping_cart = None
        self.books = []
        self.initialize_sample_book_data()

    def initialize_sample_book_data(self):
        sample_books = [
            Book(
                "Python Programming", "Gerard Nwazk", "080312345678", 29.99, 10
            ),
            Book(
                "Data Structures", "Caleb Onyemechi", "080456789012", 39.99, 5
            ),
            Book("Algorithms", "Williams Lambert", "080234567890", 49.99, 8),
        ]
        self.books.extend(sample_books)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_menu(self):
        while True:
            self.clear_screen()
            if not self.current_user:
                display_main_option()

                match input("\nEnter your choice (1-2) & 0 to exit: "):
                    case "1":
                        self.register()
                    case "2":
                        self.add_book()
                    case "0":
                        print("\nThank you for visiting! Goodbye!")
                        break
                    case _:
                        print("Invalid choice!")
                        input("Press Enter to continue...")
            else:
                display_user_menu(self)
                match input("\nEnter your choice (1-7) & 0 to exit: "):
                    case "1":
                        self.browse_books()
                    case "2":
                        self.search_books()
                    case "3":
                        self.view_cart()
                    case "4":
                        self.add_to_cart()
                    case "5":
                        self.remove_from_cart()
                    case "6":
                        self.place_order()
                    case "7":
                        self.view_order_history()
                    case "0":
                        print("\nThank you for shopping! Goodbye!")
                        break
                    case _:
                        print("Invalid choice!")
                        input("Press Enter to continue...")

    def register(self):
        try:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone = input("Enter phone (11 digits): ")
            gender = input("Enter gender (Male/Female): ")
            self.current_user = User(
                first_name, last_name, email, phone, gender
            )
            self.shopping_cart = ShoppingCart(self.current_user)
            print("Registration successful!")
            input("Press Enter to continue...")
        except ValueError as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")

    def browse_books(self):
        self.clear_screen()
        print("\n=== Available Books ===")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        input("\nPress Enter to continue...")

    def search_books(self):
        self.clear_screen()
        search_term = input("\nEnter search term: ")
        results = [
            book
            for book in self.books
            if search_term.lower() in book.title.lower()
        ]

        print("\n=== Search Results ===")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book}")
        input("\nPress Enter to continue...")

    def view_cart(self):
        self.clear_screen()
        if not self.shopping_cart.get_items():
            print("\nYour cart is empty!")
        else:
            print("\n=== Your Shopping Cart ===")
            for book, quantity in self.shopping_cart.get_items().items():
                print(
                    f"{book.title} x{quantity} - ${book.price * quantity:.2f}"
                )
            print(f"\nTotal: ${self.shopping_cart.get_total():.2f}")
        input("\nPress Enter to continue...")

    def add_to_cart(self):
        self.clear_screen()
        print("\n=== Available Books ===")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

        try:
            choice = int(input("\nEnter book number to add: ")) - 1
            if choice < 0 or choice >= len(self.books):
                raise ValueError("Invalid book number!")

            quantity = int(input("Enter quantity: "))
            book = self.books[choice]

            if self.shopping_cart.add_item(book, quantity):
                print("\nBook added to cart successfully!")
            # No else needed as error message is handled in add_item method

        except ValueError as e:
            print(f"\nError: {e}")
        input("\nPress Enter to continue...")

    def remove_from_cart(self):
        self.clear_screen()
        if not self.shopping_cart.get_items():
            print("\nYour cart is empty!")
        else:
            print("\n=== Your Shopping Cart ===")
            cart_items = list(self.shopping_cart.get_items().items())
            for i, (book, quantity) in enumerate(cart_items, 1):
                print(f"{i}. {book.title} x{quantity}")

            try:
                choice = int(input("\nEnter item number to remove: ")) - 1
                if choice < 0 or choice >= len(cart_items):
                    raise ValueError("Invalid item number!")

                book = cart_items[choice][0]
                current_quantity = cart_items[choice][1]

                quantity = int(
                    input(
                        f"Enter quantity to remove (max {current_quantity}): "
                    )
                )

                if self.shopping_cart.remove_item(book, quantity):
                    print("Item removed from cart!")
                # Error message is handled in remove_item method

            except ValueError as e:
                print(f"\nError: {e}")
        input("\nPress Enter to continue...")

    def place_order(self):
        self.clear_screen()
        if not self.shopping_cart.get_items():
            print("\nYour cart is empty!")
            input("\nPress Enter to continue...")
            return

        print("\n=== Order Summary ===")
        for book, quantity in self.shopping_cart.get_items().items():
            print(f"{book.title} x{quantity} - ${book.price * quantity:.2f}")
        print(f"\nTotal: ${self.shopping_cart.get_total():.2f}")

        confirm = input("\nConfirm order (y/n)? ").lower()
        if confirm == "y":
            order = Order(self.current_user, self.shopping_cart)

            print("\n=== Payment Methods ===")
            for i, method in enumerate(PaymentMethod, 1):
                print(f"{i}. {method.value}")

            try:
                choice = int(input("\nSelect payment method: ")) - 1
                payment_method = list(PaymentMethod)[choice]
                payment = Payment(order, payment_method)

                if payment.process_payment():
                    order.confirm_order()
                    self.shopping_cart.clear_cart()
                    print("Order placed successfully!")
                else:
                    print("Payment failed!")
            except (ValueError, IndexError):
                print("Invalid payment method!")
        input("\nPress Enter to continue...")

    def view_order_history(self):
        self.clear_screen()
        user_orders = [
            order
            for order in Order.orders
            if order._Order__user == self.current_user
        ]

        if not user_orders:
            print("\nNo orders found!")
        else:
            print("\n=== Order History ===")
            for order in user_orders:
                print(f"\nOrder ID: {order.get_order_id()}")
                print(f"Status: {order.get_status().value}")
                print(f"Total: ${order.get_total():.2f}")
                print("Items:")
                for book, quantity in order.get_items().items():
                    print(f"  - {book.title} x{quantity}")
        input("\nPress Enter to continue...")

    def logout(self):
        self.current_user = None
        self.shopping_cart = None
        print("Logged out successfully!")
        input("Press Enter to continue...")

    def add_book(self):
        self.clear_screen()
        print("\n=== Add New Book ===")
        try:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            price = float(input("Enter price: $"))
            quantity = int(input("Enter quantity in stock: "))

            new_book = Book(title, author, isbn, price, quantity)
            self.books.append(new_book)

            print("\nBook added successfully!")
        except ValueError as e:
            print(f"\nError: Invalid input - {e}")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    book_store = BookStore()
    book_store.display_menu()
