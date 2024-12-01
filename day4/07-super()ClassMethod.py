# 07-Using super() to Call Parent Class Methods
# Using `super()` automatically finds and calls the parent class methods.
# The order of resolution follows the `__mro__` attribute of the class.
# `super()` is especially suited for single inheritance.

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
        # Reinitialize subclass attributes to prevent overwriting by parent class methods.
        self.__init__()
        print(f"Using {self.kongfu} to make pancakes.")

    # Call parent class methods and attributes using explicit calls
    def make_master_cake(self):
        Master.__init__(self)  # Initialize Master class attributes
        Master.makeCake(self)  # Call Master class `makeCake` method

    def make_school_cake(self):
        School.__init__(self)  # Initialize School class attributes
        School.makeCake(self)  # Call School class `makeCake` method

    # Use super() to call parent class methods and attributes
    def make_old_cake(self):
        '''Method 1: Explicit calls (verbose and requires updates if parent class names change)'''
        # Master.__init__(self)
        # Master.makeCake(self)
        # School.__init__(self)
        # School.makeCake(self)

        '''Method 2: Using super() with parameters'''
        # super(Apprentice, self).__init__()
        # super(Apprentice, self).makeCake()

        '''Method 3: Using super() without parameters'''
        super().__init__()  # Automatically calls the next method in the MRO
        super().makeCake()  # Calls the `makeCake` method of the parent class

# 4. Create an object of the Apprentice class
apprentice = Apprentice()
apprentice.make_old_cake()
