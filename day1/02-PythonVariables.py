'''
02 - Variables
'''

'''
A variable is the name of a memory address in which data is currently stored. 
变量 - Variables   常量 - Constant
Constants are values that don't change/ don't need to be changed
'''

address  = "江苏省徐州市上海路101好9号楼809室"
like = "Kai Trump"

'''
定义变量
    变量名 = L
    int age = 18;
    age = 18
    
Variable naming customs, to meet the identifier naming rules
    *Consists of numbers, letters, underscores
    *Can't start with numbers
    *Built-In keywords can't be used
    *Strictly case-sensitive
'''


'''
Python 数据类型:

Numeric:
    int (integers)
    float (decimals)
    complex (complex numbers)
    Sequence:

list (mutable ordered collection)
    tuple (immutable ordered collection)
    range (sequence of numbers)

Text:
    str (string)

Set:
    set (unordered, unique elements)
    frozenset (immutable set)

Mapping:
    dict (key-value pairs)

Boolean:
    bool (True, False)

Binary:
    bytes, bytearray, memoryview

NoneType:
    None
'''
a = {"name":1, "sex":2, "add":3}
print(type(a))