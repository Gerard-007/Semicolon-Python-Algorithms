from User import User
import random

class Customer(User):
    customers = []
    
    def __init__(self, first_name, last_name, email, phone, gender):
        super().__init__(first_name, last_name, email, phone, gender)
        self.__customer_id = self.generate_customer_id()
        self.customers.append(self)

    def get_customer_id(self):
        return self.__customer_id

    def generate_customer_id(self):
        return f"cus-{random.randint(1000, 9999)}"

