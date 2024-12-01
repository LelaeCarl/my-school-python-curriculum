# 1. If statement
age = 18

if age == 18:
    print("Congratulations, you can go online!")

# 2. If...else statement
if age > 18:
    print("Welcome, you can go online!")
else:
    print("Your age is not suitable, please exit!")

# 3. If...elif...else statement
if age < 18:
    print("You can go online!")
elif age > 10:
    print("Study hard every day!")
else:
    print("Go play!")

# 4. Nested if statement
house = 1808080
car = 100000
money = 100000
salary = 20000

if house >= 1808080:
    print("We can try it!")
    if car >= 100000:
        print("Now I am your girlfriend!")
        if money >= 100000:
            print("Let's meet!")
            if salary > 200000:
                print("We can get the certificate now!")
            else:
                print("I have something to do, oops!")
        else:
            print("You are a good person, but it's not suitable!")
    else:
        print("I don't think we are suitable!")
else:
    print("You're not my type...")

# 5. One-line if...else statement
flag = True if age > 18 else False
print("One-line if...else statement:", flag)