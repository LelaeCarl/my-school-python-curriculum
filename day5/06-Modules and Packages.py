'''
06 - Modules and Packages
'''

'''
1. Module
A module is a Python file with a .py extension containing Python objects, functions, classes, and variables.
A module can also contain executable code blocks.
'''

'''
1.1 Importing Modules

import 模块名
from 模块名 import 功能名
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
'''

# 模块名 is the .py filename, 功能名 is a function inside the .py file

import math
print(math.sqrt(10))  # Module name, function()
from math import sqrt
print(sqrt(10))  # Function name()
from math import *
print(sin(10))  # * represents all functions
import math as mt
print(mt.sqrt(10))  # Module alias, function()
from math import sqrt as st
print(st(10))  # Function alias()

'''
1.2 Creating Modules
'''
import myModel
myModel.testA(10, 20)
from myModel import *
testA(10, 20)
import myModel as my
my.testA(20, 30)
from myModel import testA as ta
ta(10, 30)
from myModel import testA
testA(10, 20)

# Note: Prefer importing the nearest functions
from myModel2 import testA
testA(10, 20)

'''
1.3 Module Import Order
1) Current directory
2) pythonpath lookup
3) Third-party module lookup in E:/Anaconda3/lib/site-packages
'''

'''
1.4 __all__
If a module file has an __all__ variable, using `from 模块名 import *` will import only the elements listed in it.
'''
from myModel import *
testA(10, 20)
# testB(20, 30)

'''
2. Packages
'''
'''
2.1 Normal Package Import
'''
from day5.JSNU.myModel3 import testC
testC(10, 20)

'''
2.2 Set __all__ in __init__.py
'''
# Set __all__ in __init__.py, automatically called when using packages

from day5.JSNU import *
myModel3.testC(10, 20)
# myModel4.testC()
