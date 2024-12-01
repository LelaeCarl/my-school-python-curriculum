'''
1. For loop (循环)
'''

'''
2. else语法
while...else
'''

hello = "helloworld"
for i in hello:
    if i == 'e':
        print("遇到e不打印")
    break
print(i)


i= 0
while i < 7:
    print("每天吃食堂的饭菜")
    i +=1
else:
    print("回家吃饭真开心啊！！！🤧")


'''
3.For...else
'''
for i in hello:
    print(i)
else:
    print("")