# 02 - Class Attributes and Instance Attributes
'''
1. Class Attributes
1.1 Setting and Accessing Class Attributes
Class attributes are properties owned by the class itself and shared by all instances of the class.
Class attributes can be accessed via the class or instance objects.

Advantages of class attributes:
- Ensure that certain data remains consistent across all instances, so we define it as a class attribute.
- Instance attributes require a separate copy of data for each object, which uses more memory,
  whereas class attributes are shared across the class, saving memory.
'''

class Dog(object):
    tooth = 10  # Class attribute

wangcai = Dog()
xiaohei = Dog()

print("Access class attribute through class:", Dog.tooth)
print("Access class attribute through instance:", wangcai.tooth)
print("Access class attribute through instance:", xiaohei.tooth)

'''
1.2 Modifying Class Attributes
Class attributes can only be modified via the class, not through instance objects.
If you modify a class attribute via an instance, it creates a new instance attribute instead.
'''

# Modify class attribute via class
Dog.tooth = 12  # Modify class attribute
print("Access class attribute through class:", Dog.tooth)
print("Access class attribute through instance:", wangcai.tooth)
print("Access class attribute through instance:", xiaohei.tooth)

# Modify class attribute via instance object
wangcai.tooth = 20
print("Access class attribute through class:", Dog.tooth)
print("Access instance attribute through instance:", wangcai.tooth)
print("Access class attribute through another instance:", xiaohei.tooth)

'''
1.3 Instance Attributes
'''

class Dog(object):
    def __init__(self):
        self.age = 10  # Instance attribute

    def printInfo(self):
        print(self.age)

wangcai = Dog()
print("Access instance attribute through instance:", wangcai.age)
print("Access instance attribute through class:", Dog.age)  # This will throw an error
wangcai.printInfo()
