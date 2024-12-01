# 05-Subclass Calling Parent Class Methods and Attributes

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
        # To avoid overwriting subclass attributes when calling parent methods,
        # reinitialize the subclass attributes first.
        self.__init__()
        print(f"Using {self.kongfu} to make pancakes.")
    # Call Master class methods. To ensure Master class attributes are used,
    # call the Master class initializer first.
    def make_master_cake(self):
        Master.__init__(self)  # Call Master class initializer
        Master.makeCake(self)  # Call the `makeCake` method from Master class

    # Call School class methods in a similar way
    def make_school_cake(self):
        School.__init__(self)  # Call School class initializer
        School.makeCake(self)  # Call the `makeCake` method from School class

# 4. Create an object of the Apprentice class
apprentice = Apprentice()
apprentice.makeCake()          # Call the Apprentice's method
apprentice.make_master_cake()  # Call the Master class method
apprentice.make_school_cake()  # Call the School class method
apprentice.makeCake()          # Call the Apprentice's method again
