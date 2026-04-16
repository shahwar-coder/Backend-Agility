'''
Polymorphism allows same method/interface to behave differently based on object.

1. Same method name but different work
2. This is achieved by overriding
3. Improves extensibility/ flexibility
'''

'''
Polymorphism Example (Simple & Interview Ready)

Polymorphism = same method, different behavior
'''

class Payment:
    def pay(self, amount):
        print(f"Processing payment of {amount}")


class CreditCardPayment(Payment):
    def pay(self, amount):  # override
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):  # override
        print(f"Paid {amount} using UPI")


# (same interface, different behavior)
payments = [CreditCardPayment(), UPIPayment()]

for p in payments:
    p.pay(1000)


# Paid 1000 using Credit Card
# Paid 1000 using UPI


'''
What this shows:

1. Same method name:
   All classes use pay()

2. Different behavior:
   Each class implements pay() differently

3. Extensibility:
   We can add new payment types without changing existing code
'''