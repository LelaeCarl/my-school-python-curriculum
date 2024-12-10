# 03 - Class Methods and Static Methods
'''
1. Class Methods
Class methods are marked with the @classmethod decorator. For class methods,
the first parameter must be the class object (commonly named cls).

- `self` refers to the address of the instance object
- `cls` refers to the address of the class object
Example: cls.__tooth ====> Dog.__tooth
'''

class Dog(object):
    __tooth = 10  # Private class attribute

    @classmethod
    def getTooth(cls):
        return cls.__tooth


wangcai = Dog()  # Instance object
result = wangcai.getTooth()  # Instance object calling class method
print(result)

'''
2. Static Methods
Static methods are marked with the @staticmethod decorator.

Static methods:
- Do not require passing the class object or the instance object (no self/cls parameter).
- Can be accessed via both instance objects and class objects.

When a method does not need to use the instance object (e.g., instance attributes or methods) 
or the class object (e.g., class attributes, methods), a static method is defined.

Static methods eliminate unnecessary parameter passing, reducing memory usage and improving performance.
'''

class Dog(object):
    @staticmethod
    def printInfo():
        print("This is a dog class, used to create instance objects.")

wangcai = Dog()  # Instance object
wangcai.printInfo()  # Instance object accessing static method
Dog.printInfo()  # Class object accessing static method
