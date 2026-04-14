class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Whoof Whoof")

dog = Dog("Bruce", "Greyhound")
dog.bark()
print(f"Name : {dog.name}")
print(f"Breed : {dog.breed}")

# Whoof Whoof
# Name : Bruce
# Breed : Greyhound