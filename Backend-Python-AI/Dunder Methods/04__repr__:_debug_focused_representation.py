'''
TASK 2: DEBUG-FOCUSED REPRESENTATION

Write a class `Order` with:
- Attributes: order_id and status
- A __repr__ method that includes both attributes
- Create multiple Order objects and print them individually

RULES:
- __repr__ should clearly identify the object and its state
- The output should help a developer understand the object instantly

GOAL:
Learn how __repr__ is used for debugging
and why it should be unambiguous.
'''


class Order:
    "Represents an order and its current status."
    def __init__(self, order_id: str, status: str)->None:
        self.order_id = order_id
        self.status = status

    def __repr__(self)->str:
        return f"Order(order_id={self.order_id!r}, status={self.status!r})"
    
order1 = Order("A1Yuz", "Dispatched")
order2 = Order("A2Xwt", "Order Placed")

print(order1)
print(order2)

# Order(order_id='A1Yuz', status='Dispatched')
# Order(order_id='A2Xwt', status='Order Placed')