from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        self.amount = amount
    
class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card.")
    
class PaypalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Paypal Account.")

payment1 = CreditCardPayment()
payment1.make_payment(1000)

payment2 = PaypalPayment()
payment2.make_payment(500)
