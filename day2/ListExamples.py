# 01 - List

# 1. Use cases for lists
# ...

# 2. List format
# Use [..., ...] to represent a list, separating elements with commas.
# ...

# 3. Common operations with lists

# 3.1 Search
names = ['Zhang Wuji', 'Zhao Min', 'Zhou Zhiruo', 'Xiao Zhao', 'Zhu Er']

# 3.1.1 Subscript
print("3.1.1 Subscript:", names[0])

# 3.1.2 Search with index
# index() function throws an error if the element does not exist.
print("3.1.2 Function index:", names.index("Zhao Min", 0, 2))
print("3.1.2 Function count:", names.count("Zhao Min"))
print("3.1.2 Function len:", len(names))

# 3.1.3 Check if an element exists in the list
print("3.1.3 Check existence:", "Zhao Min" in names)
print("3.1.3 Check non-existence:", "Zhao Min" not in names)

# 3.2 Add

# 3.2.1 append() Add an element to the end of the list
names.append("Zhang Sanfeng")
print("3.2.1 append():", names)

# 3.2.2 extend() Add multiple elements to the list
lt = ["Zhang Cuishan", "Yin Susu", "Zhang Wuji", "Zhang Sanfeng"]
names.extend(lt)
print("3.2.2 extend():", names)

# 3.2.3 insert() Insert an element at a specified position
names.insert(8, "Fan Yao")
print("3.2.3 insert():", names)

# 3.3 Remove

# 3.3.1 del Delete by index
# del names
del names[0]
print("3.3.1 del:", names)

# 3.3.2 pop Remove and return the element at the specified index (default is the last element)
# Returns the removed value
popNames = names.pop(8)
print("3.3.2 pop result:", popNames)
print("3.3.2 pop():", names)

# 3.3.3 remove() Remove the first occurrence of a specified element
# Removes the first matching element
names.remove("Zhang Cuishan")
print("3.3.3 remove():", names)

# 3.3.4 clear() Clear the list
# names.clear()
# print("3.3.4 clear():", names)

# 3.4 Modify

# 3.4.1 Modify the element at a specified index
names[0] = "Liu Meitong"
print("3.4.1 Modify element at index:", names)

# 3.4.2 Reverse
numList = [10, 18, 20, 30, 27, 9]
numList.reverse()
print("3.4.2 reverse():", numList)

# 3.4.3 Sort
# Sorts the list
# False is ascending order, True is descending order. 'key' specifies a custom sorting rule.
numList.sort(reverse=True)
print("3.4.3 sort():", numList)

# 3.5 Copy
# Copy list elements
# Shallow copy only copies references to the values.
# Deep copy creates a new memory space to store the copied values.
numList2 = numList.copy()
print("3.5 copy():", numList2)

print("Address of numList:", id(numList))
print("Address of numList2:", id(numList2))

numList3 = numList2
print("Address of numList3:", id(numList3))
