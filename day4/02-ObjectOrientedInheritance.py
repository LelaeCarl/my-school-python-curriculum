# 02-Object-Oriented Inheritance

# 1. Concept of Inheritance
# In Python, all classes inherit from the `object` class by default.
# The `object` class is the top-level or base class.
# Other subclasses are called derived classes.
# Attributes and functions from the parent class can be accessed and used by the child class.

# 2. Single Inheritance
# Inherits from one parent class.

# 1. Master Class
class Master(object):
    def __init__(self):
        self.kongfu = "[Traditional Pancake Recipe]"
    def makeCake(self):
        print(f"Using {self.kongfu} to make pancakes.")

# 2. Apprentice Class inheriting from Master
class Apprentice(Master):
    pass

# 3. Create an object of the Apprentice class
apprentice = Apprentice()
print("2. Single Inheritance - Accessing parent class attribute:", apprentice.kongfu)
# Single Inheritance - Calling parent class function
apprentice.makeCake()
