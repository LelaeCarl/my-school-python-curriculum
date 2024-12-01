# 04 - Scope of Variables

'''
1. The Scope of Variables
   - Variables can be divided into local and global variables.
     1) Local variables: Defined inside a function and can only be used within that function.
     2) Global variables: Defined outside any function and can be used throughout the script.
   - Local variables take precedence over global variables if they have the same name.
   - Use the global keyword to declare global variables within a function.
'''

# 2. Global and Local Variables

# 2.1 Modifying global variables in a function
age = 100
print("Before testA():", id(age))
print("Before testA():", age)

def testA():
    global age
    age = 200
    print("Inside testA():", id(age))
    print("Inside testA():", age)

testA()
print("After testA():", id(age))
print("After testA():", age)

# 2.2 Using global variables to control function behavior
glNum = 100

def testC():
    global glNum
    glNum = 200

print("Before testC():", glNum)
testC()
print("After testC():", glNum)

'''
3. Returning Values
   - Functions can have multiple return values.
   - Use return to return one or more values, separated by commas.
'''

def test():
    return 10, 20

num = test()
print("Single return value:", num)

def get_test():
    return [10, 20], (30, 40)

print("Multiple return values:", get_test())

'''
4. Function Parameters
   - Functions can have fixed or variable-length parameters.
'''

# 4.1 Fixed parameters
def getInfo(name, age, sex):
    print(f"Name: {name}, Age: {age}, Sex: {sex}")

getInfo("Alice", 18, "Female")

# 4.2 Default parameters
def getInfo2(name, age, sex="Male"):
    print(f"Name: {name}, Age: {age}, Sex: {sex}")

getInfo2("Bob", 20)
getInfo2("Jane", 19, "Female")

# 4.3 Variable-length positional parameters (*args)
def getInfo4(*args):
    print("Arguments (args):", args)

getInfo4(18, 20, "Male")

# 4.4 Variable-length keyword parameters (**kwargs)
def getInfo5(**kwargs):
    print("Keyword Arguments (kwargs):", kwargs)

getInfo5(name="Alice", age=19, sex="Female")

'''
5. Functions Returning Values
'''

# 5.1 Returning multiple values
def getTuple():
    return 100, 200

num1, num2 = getTuple()
print(f"Values from tuple: num1={num1}, num2={num2}")

def getDict():
    return {"name": "Jack", "age": 18}

data = getDict()
print(f"Values from dict: name={data['name']}, age={data['age']}")

# 5.2 Returning references
a, b = 100, 200
print("Before swap: a =", a, "b =", b)

a, b = b, a
print("After swap: a =", a, "b =", b)

'''
6. References
'''

# 6.1 Passing immutable objects
def testH(a):
    print("Before modification:", id(a))
    a = 200
    print("After modification:", id(a))

b = 100
print("Global variable before:", id(b))
testH(b)

# 6.2 Passing mutable objects
lst = [10, 20]
print("Global variable before:", id(lst))
testH(lst)

'''
7. Function Design Principles
   - Functions should follow the principles of minimal scope and single responsibility.
   - Avoid excessive parameter lists; use default parameters or keyword arguments when necessary.
   - Design clear and maintainable functions that perform specific tasks effectively.
'''
