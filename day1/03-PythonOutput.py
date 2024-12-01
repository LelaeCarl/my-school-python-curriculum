# 03 - Python Output

# 1.1 %s
age = 67
name = "Logan Miller"
salary = 100000.8888

print("My name is %s" % name)
print(f"My name is {name}")  # Introduced in Python 3.6
print("My name is {}".format(name))

# 1.2 %d
print("My age is %d" % age)

# 1.3 Multiple Variables Output
print("My name is %s, and my age is %d" % (name, age))
print(f"My name is {name}, and my age is {age}")
print("My name is {}, and my age is {}".format(name, age))

# 1.4 Multiple Calculations Output
print("My name is %s, and my age next year will be %d" % (name, age + 1))

# 1.5 Formatting Tips
print("My salary is %.2f" % salary)
print("My age is %4d" % age)
print("My age is %04d" % age)

# 1.6 Convert to String
print("My name is %s\nMy age is %d\nMy salary is %.2f" % (name, age, salary))
print(f"My name is {name}\tAge: {age}\tSalary: %.2f" % salary)

# 1.7 Output Without Line Break
# print("", end="") Eliminates automatic line breaks
print("Today's weather is really nice", end="!!!!")
print("Today's weather is really not good")
