# 1. while loop
# Basic structure
# While condition is true, execute the following code block

i = 0
while i < 100:
    print("I was wrong!")
    i += 1

print("Task complete!")

# 2. while loop applications
# 2.1 Calculate the sum of numbers from 1 to 100

i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print("Sum of numbers from 1 to 100:", result)

# 2.2 Calculate the sum of even numbers from 1 to 100

i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print("Sum of even numbers from 1 to 100:", result)

# 3. break and continue
# break: Exit the loop immediately
# continue: Skip the current iteration and continue with the next one

# 4. Nested while loops
# A while loop within another while loop

day = 0
while day < 3:
    i = 0
    while i < 10:
        print("I was wrong!")
        i += 1
    print("Day {} punishment finished!".format(day + 1))
    day += 1