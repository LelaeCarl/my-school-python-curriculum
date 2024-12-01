# 09-Accessing and Modifying Private Attributes
# Private attributes can be accessed or modified using public methods.

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

    # Public method to get the value of the private attribute
    def getMoney(self):
        return self.__money

    # Public method to modify the private attribute
    def setMoney(self, money):
        self.__money += money

    def makeCake(self):
        # Reinitialize subclass attributes before using them
        self.__init__()
        print(f"Using {self.kongfu} to make pancakes.")

    def make_master_cake(self):
        Master.__init__(self)  # Initialize Master class attributes
        Master.makeCake(self)  # Call Master class `makeCake` method

    def make_school_cake(self):
        School.__init__(self)  # Initialize School class attributes
        School.makeCake(self)  # Call School class `makeCake` method

# 4. Grandchild Class
class Grandchild(Apprentice):
    pass

# 5. Create an object of the Apprentice class
apprentice = Apprentice()
print("Initial private money value:", apprentice.getMoney())  # Access private attribute using a public method
apprentice.setMoney(500)  # Modify the private attribute using a public method
print("Updated private money value:", apprentice.getMoney())
