from datetime import datetime
from enum import Enum

class PaymentMethod(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    BANK_TRANSFER = "BANK_TRANSFER"
    CASH = "CASH"

class PaymentStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

class Payment:
    payments = []
    
    def __init__(self, order, payment_method):
        self.__payment_id = len(Payment.payments) + 1
        self.__order = order
        self.__amount = order.get_total()
        self.__payment_method = payment_method
        self.__status = PaymentStatus.PENDING
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
        Payment.payments.append(self)

    def process_payment(self):
        try:
            self.__status = PaymentStatus.COMPLETED
            self.__updated_at = datetime.now()
            return True
        except Exception as e:
            self.__status = PaymentStatus.FAILED
            self.__updated_at = datetime.now()
            return False

    def refund_payment(self):
        if self.__status == PaymentStatus.COMPLETED:
            self.__status = PaymentStatus.REFUNDED
            self.__updated_at = datetime.now()
            return True
        return False

    def get_payment_id(self):
        return self.__payment_id

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    def get_payment_method(self):
        return self.__payment_method

    def __str__(self):
        return f"""
            Payment ID: {self.__payment_id}
            Amount: ${self.__amount:.2f}
            Method: {self.__payment_method.value}
            Status: {self.__status.value}
            Created: {self.__created_at}
            Updated: {self.__updated_at}
        """
