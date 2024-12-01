# 03-Multiple Inheritance
# Notes:
# When a class has multiple parent classes, it will use the attributes and methods of the first parent class by default if there are conflicts.

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
    pass

# 4. Create an object of the Apprentice class
apprentice = Apprentice()
print("Accessing attributes from Apprentice class:", apprentice.kongfu)
# Calling methods from Apprentice class
apprentice.makeCake()
