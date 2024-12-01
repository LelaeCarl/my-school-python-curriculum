# 03 - Functions

'''
1. Purpose of Functions
   In the development process, functions allow for more efficient code reuse.
'''

'''
2. Steps to Use Functions
   1) Define a function:
      def function_name(parameter_list):
          code block
   2) Call the function:
      function_name(parameter_list)
   Notes:
      - Parameters can be optional depending on the function's requirements.
      - In Python, a function must be defined before it can be used.
'''

'''
3. Function Parameters
   Formal parameters: Specified in the function definition (placeholders, not actual data).
   Actual parameters: Passed during the function call (real data).
'''

def add(a, b):
    result = a + b
    print("Result is:", result)

add(10, 20)

'''
4. Function Return Values
'''

def df(money):
    """
    Liu Bei's meal suggestions, based on budget.
    """
    if money >= 20:
        return "Soybean Beef Meal"
    elif 10 <= money < 20:
        return "Spicy Bean Vegetarian Meal"
    else:
        return "Just eat air!"

'''
5. Function Documentation
'''

def eat():
    """
    This is a placeholder for some humorous or simple documentation:
    'I eat dogs in the beginning of the month, eat dogs in the middle of the month,
    and by the end of the month, the dogs eat me.'
    """
    print("I want to eat!")

help(eat)

'''
6. Function Nesting
'''

def testB():
    print("Function B starts ----")
    print("Function B ends ----")

def testA():
    print("Function A starts ----")
    testB()
    print("Function A ends ----")

testA()
