# 04-Overriding Parent Class Methods and Attributes in a Subclass
# When a subclass and its parent class have methods or attributes with the same name,
# the subclass's methods and attributes are used by default.

# 1. Master Class
class Master(object):
    def __init__(self):
        self.kongfu = "[Traditional Pancake Recipe]"
    def makeCake(self):
        print(f"Using {self.kongfu} to make pancakes.")

# 2. School Class
class School(object):
    def __init__(self):
        self.kongfu = "[Dark Pancake Recipe]"
    def makeCake(self):
        print(f"Using {self.kongfu} to make pancakes.")

# 3. Apprentice Class
class Apprentice(Master, School):
    def __init__(self):
        self.kongfu = "[Original Pancake Recipe]"
    def makeCake(self):
        print(f"Using {self.kongfu} to make pancakes.")

# 4. Create an object of the Apprentice class
apprentice = Apprentice()
print("Subclass overriding parent class attributes and methods:", apprentice.kongfu)
apprentice.makeCake()

# Using the `__mro__` magic method to check the inheritance hierarchy
print("Inheritance hierarchy:", Apprentice.__mro__)
