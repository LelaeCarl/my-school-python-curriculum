'''
04 - Exception Handling
'''

'''
1. Syntax for Exceptions

try:
    # Code that may cause an error
except:
    # Code to execute if an exception occurs
'''
'''
2. Catch Specific Exceptions
'''
# try:
#     print(num)
# except NameError:
#     print("NameError occurred")

'''
3. Catch Multiple Specific Exceptions
'''
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError):
#     print("Caught multiple specific exceptions")

'''
4. Catch Exception Description
'''
# try:
#     print(num)
# except (NameError, ZeroDivisionError) as result:
#     print("Caught exception description:", result)

'''
5. Catch All Exceptions
'''
# try:
#     print(num)
# except Exception as result:
#     print("Caught all exceptions:", result)

'''
6. Else in Exception Handling
'''
try:
    print(1)
except Exception as result:
    print("Exception occurred:", result)
else:
    print("This is else, executed when no exception occurs")

'''
7. Finally in Exception Handling
'''
try:
    f = open("test.txt", 'r')
except Exception as result:
    f = open("test.txt", 'w')
    print("Code executed when an exception occurs")
else:
    print("Code executed when no exception occurs")
finally:
    print("Code executed no matter what")
