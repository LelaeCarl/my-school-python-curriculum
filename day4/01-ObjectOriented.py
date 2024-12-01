# 01-Object-Oriented Programming (OOP)

# 1. Understanding OOP
# Everything is an object.
# OOP is an abstraction-based programming paradigm. Many programming languages adopt this concept.
# Example: Hand-washing vs. Machine-washing
# Hand-washing involves: finding a basin => adding water => adding detergent => soaking => scrubbing => wringing out => draining => rinsing...
# Machine-washing involves: opening the washing machine => putting clothes in => adding detergent => pressing a button => drying
# OOP treats programming as managing objects. To the outside, an object is ready for use without needing to know its internal workings.
# Programming involves defining what actions an object can perform.

# 2. Classes and Objects
# The relationship between classes and objects: Use a class to create an object.

# 2.1 Understanding Classes and Objects
# A class is a generalized term for a group of things with the same characteristics and behaviors. It is an abstract concept.
# Characteristics = Attributes
# Behaviors = Methods/Functions
# A class is used to create (instantiate) objects.
# Objects are real, tangible entities created using a class.

class Cuihua():
    # Attributes
    height = 168
    weight = 100
    # Methods
    def eat(self):
        pass

# 2.2 Implementing OOP

# 2.2.1 Define a Class
# The default parent class is `object`
class Zhangsan():
    pass

class Lisi:
    pass

# 2.2.2 Create an Object
# Syntax: object_name = ClassName()
# Creating an object is also called instantiation.

# 2.2.3 `self`
# `self` refers to the calling object.
# Both `self` and the object name store memory addresses.

# 1) Define a class
class Washer():
    # 2) Define a function
    def wash(self):
        print("I can wash clothes")
        print("The `self` inside wash function:", self)

# 3) Create an object (instantiate)
w1 = Washer()
print("Value of w1:", w1)
# 4) Call the `wash` function
w1.wash()

# 3. Adding and Accessing Object Attributes
# Attributes = Characteristics
# Object attributes can be added and accessed outside the class or inside the class.

# 3.1 Add object attributes outside the class
# Syntax: object_name.attribute_name = value
w1.width = 500
w1.height = 800

# 3.2 Access object attributes outside the class
# Syntax: object_name.attribute_name
print("3.2 Access attributes outside the class:", w1.width)
print("3.2 Access attributes outside the class:", w1.height)

# 3.3 Access object attributes inside the class
class Washer2():
    def printInfo(self):
        # Access object attributes inside the class
        print("Attributes accessed inside Washer2 class:", self.width)
        print("Attributes accessed inside Washer2 class:", self.height)

# Create an object
w2 = Washer2()
# Add instance attributes
w2.width = 500
w2.height = 800
# Call the object's function
w2.printInfo()

# 4. Magic Methods
# In Python, these are special methods with specific functions.

# 4.1 `__init__()` Instantiation Method
class Washer3():
    # Magic method
    def __init__(self):
        # Add instance attributes
        self.width = 500
        self.height = 800
    def printInfo(self):
        print(f"Attributes in Washer3 class: {self.width} >>> {self.height}")

w3 = Washer3()
w3.printInfo()

class Washer4():
    # Magic method
    def __init__(self, width, height):
        # Add instance attributes
        self.width = width
        self.height = height
    def printInfo(self):
        print(f"Attributes in Washer4 class: {self.width} >>> {self.height}")

w4 = Washer4(600, 900)
w4.printInfo()

# 4.2 `__str__()` Method - Overrides default memory address printing, similar to `toString()`
class Washer5():
    # Magic method
    def __init__(self, width, height):
        # Add instance attributes
        self.width = width
        self.height = height
    # Magic method
    def __str__(self):
        return "This is a washing machine"

w5 = Washer5(600, 900)
print("Output of `__str__` method:", w5)

# 4.3 `__del__()` Method - Called when an object is deleted
class Washer6():
    # Magic method
    def __init__(self, width, height):
        # Add instance attributes
        self.width = width
        self.height = height
    # Magic method
    def __str__(self):
        return "This is a washing machine"
    # Magic method
    def __del__(self):
        print(f"The object {self} has been deleted")

w6 = Washer6(600, 900)
del w6
