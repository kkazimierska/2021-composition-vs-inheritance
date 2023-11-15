# Task. Refactor class to comply with SOLID principles.
from typing import List


class Order:
    """Order the items in shop.
    """
    def __init__(self) -> None:
        self.items: List[str] = []
        self.quantities: List[int] = []
        self.prices:List[int] = []
        self.status:str = "open"


    def add_item(self, name: str, quantity:int, price:int):
        """ Adds the item to buy.
        :param name: the name of object to buy
        :param quantity: the quantity of object to buy
        :param price: the price of object to buy
        """
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self)->int:
        """Summarize the total price to pay
        :return: The total sum.
        """
        total = 0
        for i, _ in enumerate(self.prices):
            total +=  self.quantities[i] * self.prices[i]
        return total


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 50)



from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    def set_status(self, order):
        order.status = "paid"

    @abstractmethod
    def pay(self, order):
        pass

# class PaymentProcessorSMS(PaymentProcessor):

#     @abstractmethod
#     def auth_sms(self, code):
#         pass

class Authorizer(ABC):
    
    @abstractmethod
    def is_authorized(self)->bool:
        pass

class SMSAuth(Authorizer):
    
    def __init__(self) -> None:
        self.verified = False
        
    def verify(self, code):
        print(f"Verfying code {code}")
        self.verified = True
        
    def is_authorized(self):
        return self.verified

# TODO: Impletemnt Robot Authorizer
class Robot(Authorizer):
    pass

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int, authorizer:Authorizer) -> None:
        super().__init__()
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Payment not authorized.")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.set_status(order)

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int) -> None:
        super().__init__()
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.set_status(order)

auth = SMSAuth()
auth.verify(3456)
payment_processor = DebitPaymentProcessor(1234, auth)
payment_processor.pay(order)