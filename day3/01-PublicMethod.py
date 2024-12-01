'''
01-公共方法
'''

'''
1.运算符
    +           字符串、列表、元组
    *           字符串、列表、元组
    in          字符串、列表、元组、字典
    not in      字符串、列表、元组、字典
'''
# 1.1 +  合并
str1 = "张无忌"
str2 = "赵敏"
print("1.1 + 合并:",str1+str2)

lt1 = [10,20]
lt2 = [30,40]
print("1.1 + 合并:",lt1+lt2)

tp1 = (10,20)
tp2 = (30,40)
print("1.1 + 合并:",tp1 + tp2)

# 1.2 * 复制
print("="*10)

'''
2.公共方法
    len()
    del或del()
    max()
    min()
    range(start,end,step)   范围,左闭右开原则
    enumerate               既可以得到下标,也是得到元素值,默认起始值0
'''
# 2.1 max()
lt3 = [10,18,20,39,8]
print("2.1 max()求取最大值:",max(lt3))

# 2.2 min()
print("2.2 min()求取最小值:",min(lt3))

# 2.3 range()
for i in range(0,len(lt3),2):
    print("2.3 range():",lt3[i])

# 2.4 enumerate
for i,num in enumerate(lt3):
    print(f"2.4 enumerate:{i}>>>{num}")

'''
3.容器类型转换
list()
tuple()
set()
'''
# 3.1 list
hello = "helloworld"
print("3.1 list类型:",list(hello))

# 3.2 tuple
print("3.2 tuple类型:",tuple(hello))

# 3.3 set
print("3.3 set类型:",set(hello))