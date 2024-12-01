# 10-Object-Oriented Programming - Additional Concepts

# * Encapsulation
#   - Encapsulation refers to the practice of bundling attributes and methods within a class.
#   - Attributes and methods can also be given private access using encapsulation.

# Example: Encapsulation
class EncapsulationExample:
    def __init__(self):
        self.public_attribute = "I am public"
        self.__private_attribute = "I am private"

    def public_method(self):
        print("This is a public method")

    def __private_method(self):
        print("This is a private method")

    def access_private(self):
        print("Accessing private attribute:", self.__private_attribute)
        self.__private_method()

encap = EncapsulationExample()
print(encap.public_attribute)
encap.public_method()
encap.access_private()
# The following would raise an error:
# print(encap.__private_attribute)
# encap.__private_method()

# * Inheritance
#   - Subclasses automatically inherit all attributes and methods from the parent class.
#   - Subclasses can override parent class attributes and methods.

# Example: Inheritance
class Parent:
    def __init__(self):
        self.attribute = "I am from the Parent class"

    def show_message(self):
        print("This is a message from the Parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.attribute = "I am from the Child class"

    def show_message(self):
        print("This is a message from the Child class")

child = Child()
print(child.attribute)
child.show_message()

# * Polymorphism
#   - Polymorphism allows the same method to have different behaviors based on the object it is called on.

# Example: Polymorphism
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
