# 02 - Comprehensions

# 1. List Comprehensions
# Use list comprehensions to generate lists with patterns or controlled rules

# 1.1 Basic Version
lt1 = [i for i in range(10)]
print("1.1 Basic Version:", lt1)

# 1.2 With If Condition
lt2 = [i for i in range(10) if i % 2 == 0]
print("1.2 With If Condition:", lt2)

# 1.3 With Nested Loops
lt3 = [(i, j) for i in range(10) for j in range(5)]
print("1.3 With Nested Loops:", lt3)

# 2. Dictionary Comprehensions

# 2.1 Basic Version
dt1 = {i: i * 2 for i in range(5)}
print("2.1 Basic Version:", dt1)

# 2.2 Merge Two Lists into a Dictionary
lt4 = ['name', 'age', 'gender']
lt5 = ['John Doe', 20, 'Male']
dt2 = {lt4[i]: lt5[i] for i in range(len(lt4))}
print("2.2 Merge Two Lists into a Dictionary:", dt2)

# 2.3 Extract Data from a Dictionary
dt3 = {'Chen': 10000, 'Zhang': 20000, 'Wang': 30000, 'Shi': 35000}
dt4 = {key: value for key, value in dt3.items() if value >= 20000}
print("2.3 Extract Data from a Dictionary:", dt4)

# 3. Set Comprehensions
st1 = {i ** 2 for i in range(5)}
print("3. Set Comprehensions:", st1)
