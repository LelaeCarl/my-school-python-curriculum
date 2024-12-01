# 05 - Python Data Type Conversion

# 1. Functions for data type conversion
# int(x): Convert x to an integer
# float(x): Convert x to a float
# complex(real, [imag]): Create a complex number with real as the real part and imag as the imaginary part
# str(x): Convert object x to a string
# repr(x): Convert object x to an expression-style string
# eval(str): Evaluate a string containing a Python expression and return an object
# tuple(s): Convert a sequence to a tuple
# list(s): Convert a sequence to a list
# chr(x): Convert an integer to a Unicode character
# ord(x): Convert a character to its integer (ASCII or Unicode) value
# oct(x): Convert an integer to an octal string
# bin(x): Convert an integer to a binary string

# 1.1 Receiving input from the user
# number = input("Please enter your lucky number: ")

# 1.2 Display the input
# print(f"Your lucky number is: {number}")

# 1.3 Check the data type of the user input
# print("Data type is:", type(number))

# 1.4 Convert to integer
# print(type(int(number)))

# 2. Demonstration of data type conversion

# 2.1 int conversion
age = "18"
print("2.1 int conversion: %d" % int(age))

# 2.2 str conversion
num2 = 18
print("2.2 str conversion: %s" % str(num2))

# 2.3 tuple conversion
lt1 = [10, 20, 30]
print("2.3 tuple conversion:", type(tuple(lt1)))

# 2.4 list conversion
tp1 = (10, 20, 30)
print("2.4 list conversion:", type(list(tp1)))

# 2.5 eval: Convert strings into Python expressions and check their original data types
str1 = "10"
str2 = "[1,2,3]"
str3 = "(100,200,300)"
print("eval conversion result 1:", type(eval(str1)))
print("eval conversion result 2:", type(eval(str2)))
print("eval conversion result 3:", type(eval(str3)))

# 2.6 repr: Convert to expression-style string
str4 = "30 > 20"
print("repr conversion result:", repr(str4))
