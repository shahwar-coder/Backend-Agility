'''
Abstraction hides implementation details and exposes only necessary functionality.

1. Hides Complexity:
- show only essential features
- hides internal implementation
- user does not need to know how things work, just how to use

2. Focus on What, not how.

3. Improves Maintainability/ Reusability:
- internal logic can be later changes, without affecting users
'''

from abc import ABC, abstractmethod

# Abstract class (focus only this)
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass # pay is the `what` user has to focus on

# Concrete class (hides implementation details)
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of amount {amount} made by Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of amount {amount} made by UPI")


payment1 = CreditCardPayment()
payment2 = UPIPayment()

payment1.pay(8000)
payment2.pay(6000)