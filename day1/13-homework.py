'''
13-课后作业
需求:
    1.随机产生1-100之间的随机数
    2.使用input函数输入数值
    3.使用while循环进行判断比较 知道猜对结束
    4.使用if判断 大了 小了 对了 错了 几种情况
        错了指的是  超过100  低于1 输入的不是数字
'''
import random

target_number = random.randint(1, 100)
print(f"The number to guess is: {target_number}")  # Print the number for reference

print("Guess the number! It's between 1 and 100.")

while True:

    user_input = input("Enter your guess: ")


    if not user_input.isdigit():  # Check if input is not a number
        print("Wrong! You need to enter a valid number.")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 100:  # Check if number is out of range
        print("❌Wrong! Your guess must be between 1 and 100.")
    elif guess > target_number:  # Guess is too high
        print("❌Too high!")
    elif guess < target_number:  # Guess is too low
        print("❌Too low!")
    else:  # Guess is correct
        print("✅Correct! You guessed the number.✅")
        break
