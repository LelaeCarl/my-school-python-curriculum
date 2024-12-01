# 06 - Python Operators

# 1. Arithmetic Operators
# + - * / // % ** ()
# Note: Operator precedence:
# Parentheses () > Exponentiation ** > Multiplication/Division // / % > Addition/Subtraction + -

num1 = 9
num2 = 4
print("1.1 Integer division:", num1 // num2)
print("1.2 Modulus:", num1 % num2)
print("1.3 Exponentiation:", num1 ** 2)

# 2. Assignment Operators
# =

# 2.1 Assigning a value to a single variable
num3 = 30

# 2.2 Assigning multiple variables at once
num4, float1, str1 = 10, 0.5, "helloWorld"

# 2.3 Assigning the same value to multiple variables
a = b = 10
print("Value of a:", a)
print("Value of b:", b)

# 3. Compound Assignment Operators
# += -= *= /= //= %= **=

# 3.1 Example of +=
# Equivalent to num4 = num4 + 10
num4 += 10

# 4. Comparison Operators
# == != > < >= <=

# 5. Logical Operators
# and or not
# Note:
# - Short-circuit behavior for `and` and `or`

# 5.1 Using `and`
house = 1000000
car = 200000
print("5.1 and:", house >= 1000000 and car >= 200000)

# 5.2 Using `or`
print("5.2 or:", house >= 1000000 or car >= 200000)

# 5.3 Using `not`
print("5.3 not:", not "male")
