# 04-Dictionaries

# 1. Applications of Dictionaries

# 2. Dictionary Syntax
#    Use curly braces, colons, and commas for separation
#    key:value pairs
student = {"name": "Zhang Sanfeng", "age": 120, "sex": "Male"}

# 3. Common Dictionary Operations

# 3.1 Add
# Dictionary[key] = value
student["email"] = "zsf@163.com"
print("3.1 Add:", student)

# 3.2 Delete
# 3.2.1 del() Deletes the dictionary or a specific key-value pair
del student['email']
print("3.2.1 del delete:", student)

# 3.2.2 clear() Clears the dictionary
student.clear()
print("3.2.2 clear clear:", student)

# 3.3 Modify
# Dictionary[key] = value
student = {"name": "Zhang Sanfeng", "age": 120, "sex": "Male"}
student["age"] = 100
print("3.3 Modify:", student)

# 3.4 Retrieve
# 3.4.1 Retrieve by key
print("3.4.1 Retrieve by key:", student['name'])

# 3.4.2 Retrieve using get
print("3.4.2 Retrieve using get:", student.get("age"))

# 3.4.3 Retrieve all keys using keys() - Returns a list
print("3.4.3 Retrieve all keys:", student.keys())

# 3.4.4 Retrieve all values using values() - Returns a list
print("3.4.4 Retrieve all values:", student.values())

# 3.4.5 Retrieve all key-value pairs using items()
# Key-value pairs are displayed as tuples in a list
print("3.4.5 Retrieve all key-value pairs:", student.items())

# 4. Looping Through a Dictionary

# 4.1 Loop through dictionary keys
for key in student.keys():
    print("4.1 Loop through dictionary keys:", key)

# 4.2 Loop through dictionary values
for value in student.values():
    print("4.2 Loop through dictionary values:", value)

# 4.3 Loop through dictionary elements (key-value pairs)
for item in student.items():
    print("4.3 Loop through dictionary items:", item)

# 4.4 Loop through dictionary keys and values
for key, value in student.items():
    print(f"4.4 Loop through dictionary key-value: {key} : {value}")
