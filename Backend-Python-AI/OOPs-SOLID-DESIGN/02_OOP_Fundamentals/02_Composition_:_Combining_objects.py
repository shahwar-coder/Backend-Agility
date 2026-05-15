class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof Whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner1 = Owner("Shahwar", "Bengaluru", "1234567890")
dog1 = Dog("Bruce", "Greyhound", owner1)
dog1.bark()
print(f"Name : {dog1.name}")
print(f"Breed : {dog1.breed}")
print(f"Owner (name) : {dog1.owner.name}")
print(f"Owner (address) : {dog1.owner.address}")
print(f"Owner (contact number) : {dog1.owner.contact_number}")

# Whoof Whoof
# Name : Bruce
# Breed : Greyhound
# Owner (name) : Shahwar
# Owner (address) : Bengaluru
# Owner (contact number) : 1234567890



'''
This code demonstrates a simple example of **composition in OOP**.

- We define two classes: Dog and Owner.
- The Owner class stores details about a dog’s owner (name, address, contact).
- The Dog class stores details about the dog (name, breed) and also holds
  a reference to an Owner object.

Key Idea:
👉 A Dog "has an" Owner → This is composition.

Flow:
1. Create an Owner object (owner1).
2. Pass this owner object while creating a Dog object (dog1).
3. Now dog1 can access owner details using dot notation:
   dog1.owner.name, dog1.owner.address, etc.

Methods:
- bark() → prints "Whoof Whoof"

Output:
- Dog details are printed.
- Owner details are accessed through the Dog object.

Why important:
👉 This pattern is widely used in backend systems where one entity
   is linked to another (e.g., User → Orders, Blog → Author).
'''