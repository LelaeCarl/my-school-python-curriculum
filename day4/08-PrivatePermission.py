# 08-Private Attributes and Methods
# - Private attributes and methods can only be accessed or modified within the class.
# - Objects cannot directly access private attributes and methods.
# - Child classes cannot inherit private attributes and methods from the parent class.

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
        # Define a private attribute
        self.__money = 1000000

    # Define a private method
    def __printInfo(self):
        print("Private method accessing:", self.kongfu)
        print("Private method accessing private attribute:", self.__money)

    def makeCake(self):
        # Reinitialize subclass attributes before using them
        self.__init__()
        print(f"Using {self.kongfu} to make pancakes.")

    def make_master_cake(self):
        Master.__init__(self)  # Call Master class initializer
        Master.makeCake(self)  # Call Master class `makeCake` method

    def make_school_cake(self):
        School.__init__(self)  # Call School class initializer
        School.makeCake(self)  # Call School class `makeCake` method

# 4. Grandchild Class
class Grandchild(Apprentice):
    pass

# 5. Create an object of the Grandchild class
grandchild = Grandchild()
# Attempting to access private attributes or methods from the parent class will result in an error:
# print(grandchild.__money)  # Cannot access parent's private attribute
# grandchild.__printInfo()  # Cannot access parent's private method

# 6. Create an object of the Apprentice class
apprentice = Apprentice()
# Attempting to access private attributes or methods within the same class also fails:
# print(apprentice.__money)  # Cannot access private attribute
# apprentice.__printInfo()  # Cannot access private method
