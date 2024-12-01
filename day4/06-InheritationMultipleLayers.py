# 06-Multi-Level Inheritance

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
        # If a parent class's method or attribute is called first,
        # it may overwrite the subclass attributes. To prevent this, reinitialize the subclass.
        self.__init__()
        print(f"Using {self.kongfu} to make pancakes.")
    # Call Master class methods. Ensure Master-specific attributes are used by calling its initializer.
    def make_master_cake(self):
        Master.__init__(self)  # Call Master class initializer
        Master.makeCake(self)  # Call the `makeCake` method from Master class

    # Call School class methods in a similar way
    def make_school_cake(self):
        School.__init__(self)  # Call School class initializer
        School.makeCake(self)  # Call the `makeCake` method from School class

# 4. Grandchild Class
class Grandchild(Apprentice):
    pass

# 5. Create an object of the Grandchild class
grandchild = Grandchild()
grandchild.makeCake()          # Call the method from Apprentice
grandchild.make_master_cake()  # Call the method from Master
grandchild.make_school_cake()  # Call the method from School
