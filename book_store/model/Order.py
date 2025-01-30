from datetime import datetime
from enum import Enum

class OrderStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class Order:
    orders = []
    
    def __init__(self, user, shopping_cart):
        self.__order_id = len(Order.orders) + 1
        self.__user = user
        self.__items = shopping_cart.get_items().copy()
        self.__total = shopping_cart.get_total()
        self.__status = OrderStatus.PENDING
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        Order.orders.append(self)

    def confirm_order(self):
        self.__status = OrderStatus.CONFIRMED
        self.__updated_at = datetime.now()

    def ship_order(self):
        self.__status = OrderStatus.SHIPPED
        self.__updated_at = datetime.now()

    def deliver_order(self):
        self.__status = OrderStatus.DELIVERED
        self.__updated_at = datetime.now()

    def cancel_order(self):
        self.__status = OrderStatus.CANCELLED
        self.__updated_at = datetime.now()

    def get_order_id(self):
        return self.__order_id

    def get_status(self):
        return self.__status

    def get_total(self):
        return self.__total

    def get_items(self):
        return self.__items
