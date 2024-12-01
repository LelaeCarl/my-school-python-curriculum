# 06-Sets

# 1. Creating Sets
#    Use {} or set()
#    Notes:
#    1. To create an empty set, you must use set()
#    2. Sets automatically remove duplicate data
#    3. Sets are unordered, so indexing is not supported
st = set()
st1 = {10, 20, 30, 40, 50}

# 2. Common Set Operations
# 2.1 Adding Data
# 2.1.1 add()
st1.add(60)
st1.add(20)
print("2.1.1 add function:", st1)

# 2.1.2 update() Append a sequence of data
st2 = {100, 200}
st1.update(st2)
print("2.1.2 update function:", st1)

# 2.2 Removing Data
# 2.2.1 remove() Removes an element from the set; raises an error if the element doesn't exist
st1.remove(10)
print("2.2.1 remove function:", st1)

# 2.2.2 discard() Removes the specified element from the set; does not raise an error if the element doesn't exist
st1.discard(400)
print("2.2.2 discard function:", st1)

# 2.2.3 pop() Removes and returns an arbitrary element from the set
popValue = st1.pop()
print("2.2.3 pop function:", st1)
print("2.2.3 popValue:", popValue)

# 2.3 Searching in a Set
# 2.3.1 in - Check if a value exists in the set
print("2.3.1 in check:", 10 in st1)

# 2.3.2 not in - Check if a value does not exist in the set
print("2.3.2 not in check:", 20 not in st1)
