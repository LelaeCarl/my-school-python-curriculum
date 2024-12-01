# 03-Tuples

# 1. Applications of Tuples

# 2. Defining a Tuple
#    Use parentheses + commas to separate data
#    Data can be of different types
#    The elements in a tuple cannot be modified
tp1 = ("Zhang Sanfeng", 120, 'Male')

# 3. Common Tuple Operations

# 3.1 Accessing data by index
print("3.1 Accessing data by index:", tp1[0])

# 3.2 Using index to find data
print("3.2 Using index to find data:", tp1.index(120))

# 3.3 Using count to find data
print("3.3 Using count to find data:", tp1.count("Male"))

# 3.4 len
print("3.4 len to find the number of elements:", len(tp1))
