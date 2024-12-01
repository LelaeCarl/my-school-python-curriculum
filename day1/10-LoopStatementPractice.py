'''
1. use while-loop to...
'''

row = 1
while row <= 5:
    column = 1
    while column <= 5:
        print("💩", end=" ")
        column += 1
    print()
    row += 1

print()

# 2. Right-angled triangle of stars
row = 1
while row <= 5:
    column = 1
    while column <= row:
        print("💩", end=" ")
        column += 1
    print()
    row += 1

print()

# 3. Multiplication table (up to 9x9)
row = 1
while row <= 9:
    column = 1
    while column <= row:
        print(f"{column}*{row}={column*row}", end="\t")
        column += 1
    print()
    row += 1