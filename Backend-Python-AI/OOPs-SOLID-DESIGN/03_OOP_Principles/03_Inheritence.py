'''
Inheritence allows a class to reuse and extend another class's functionality.

1. Code reusability
2. Extensibility
3. Can show hierarchy (eg. Dog is an Animal), so better design
'''

'''
Inheritance Example (Real-world: Payment System)

Parent class defines common behavior,
child classes extend or customize it.
'''

# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting")


# Child class 1
class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving")


# Child class 2
class Bike(Vehicle):
    def ride(self):
        print(f"{self.brand} bike is riding")

c = Car("Toyota")
b = Bike("Yamaha")

c.start()   # inherited
c.drive()   # own method

b.start()   # inherited
b.ride()    # own method


'''
What this shows:

1. Code Reusability:
   start() is reused from Vehicle

2. Extensibility:
   Car adds drive(), Bike adds ride()

3. Is-A Relationship:
   Car is a Vehicle
   Bike is a Vehicle
'''