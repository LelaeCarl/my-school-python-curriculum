'''
12-Strings
'''
'''
1. String Syntax
    "" or '' or """ """ or ''' '''
'''
str1 = "Zhang Sanfeng"
str2 = 'Zhang Wuji'
str3 = """Zhang Cuishan"""
str4 = '''Zhang Xueyou'''
print("Type 1:", type(str1))
print("Type 2:", type(str2))
print("Type 3:", type(str3))
print("Type 4:", type(str4))

'''
2. Indexing
    Starts from 0, ends at len(sequence)-1
    Use [integer] to indicate the index
'''
print("Index:", str1[2])
print("Index:", str1[len(str1) - 1])

'''
3. Slicing
    Extract a part of the sequence
    Supported by strings, lists, and tuples
    sequence[start_index:end_index:step]
    Notes:
        1. Left-inclusive, right-exclusive rule: start_index <= x < end_index
        2. Start and end indices can be positive or negative integers
        3. Step determines the interval, can be positive or negative, default is 1
        4. If start is omitted, default is 0
        5. If end is omitted, default is the last element
        6. Negative indices count from the end, starting from -1
'''
address = "Jiangsu Province, Xuzhou City, Shanghai Road 101"
# 3.1 Xuzhou City
print("3.1 Xuzhou City:", address[3:6])
# 3.2 Jiangsu Province
print("3.2 Jiangsu Province:", address[:3])
# 3.3 101
print("3.3 101:", address[9:])
# 3.4 Entire string
print("3.4 Entire string:", address[:])
# 3.5 Alternate characters
print("3.5 Alternate characters:", address[::2])
# 3.6 Exclude last character
print("3.6 Exclude last character:", address[:-1])
# 3.7 101
print("3.7 101:", address[-4:])
# 3.8 Reverse string
print("3.8 Reverse string:", address[::-1])

'''
4. Common Methods
'''
'''
4.1 Search
'''
'''
4.1.1 find() Checks if a substring exists in the string
    Returns the index if found, -1 otherwise
    string_sequence.find(substring, start_index, end_index)
'''
print("4.1.1 find() function", address.find("101"))
print("4.1.1 find() function", address.find("909"))

'''
4.1.2 index() Checks if a substring exists in the string
    Returns the index if found, raises an exception otherwise
'''
print("4.1.2 index() function", address.index("101"))
# print("4.1.2 index() function", address.index("909"))

'''
4.1.3 rfind() Searches from right to left
'''
hello = "Hello 123 World 123"
print("4.1.3 rfind() function", hello.rfind("123"))

'''
4.1.4 rindex() Searches from right to left
'''
print("4.1.4 rindex() function", hello.rindex("123"))

'''
4.1.5 count() Returns the number of occurrences of a substring
'''
print("4.1.5 count() function", hello.count("123"))

'''
4.2 Modify
'''
'''
4.2.1 replace() Replace substrings
    string_sequence.replace(old_substring, new_substring, replace_count)
'''
print("4.2.1 replace() replace", hello.replace("123", "456"))

'''
4.2.2 split() Split the string by a specified character
    string_sequence.split(separator, num)
    Notes:
        If num is not specified, it splits all occurrences
'''
print("4.2.2 split() function:", hello.split("123"))

'''
4.2.3 join() Combine multiple strings into one using a separator
'''
lt = ["Zhang Wuji", "Zhao Min", "Zhou Zhiruo", "Xiao Zhao", "Zhu'er"]
str5 = "❤️".join(lt)
print("4.2.3 join() function:", str5)

'''
4.2.4 capitalize() Capitalizes the first character of the string
'''
hello = "helloworld"
print("4.2.4 capitalize() function:", hello.capitalize())

'''
4.2.5 title() Capitalizes the first letter of each word
'''
hello = "hello world"
print("4.2.5 title() function:", hello.title())

'''
4.2.6 lower() Converts all uppercase letters to lowercase
'''
hello = "HELLOWORLD"
print("4.2.6 lower() function:", hello.lower())

'''
4.2.7 upper() Converts all lowercase letters to uppercase
'''
hello = "helloworld"
print("4.2.7 upper() function:", hello.upper())

'''
4.2.8 lstrip() Removes whitespace from the left side
'''
hello = "      helloworld"
print("4.2.8 lstrip() function:", hello.lstrip())

'''
4.2.9 rstrip() Removes whitespace from the right side
'''
hello = "helloworld       "
print("4.2.9 rstrip() function:", hello.rstrip(), end="#\n")

'''
4.2.10 strip() Removes whitespace from both sides
'''
hello = "     helloworld      "
print("4.2.10 strip():", hello.strip(), end="#\n")

'''
4.2.11 ljust() Left-aligns the string, filling the rest with a specified character
    string_sequence.ljust(length, fill_char)
'''
hello = "hello"
print("4.2.11 ljust() function:", hello.ljust(10, "#"))

'''
4.2.12 rjust() Right-aligns the string
'''
hello = "hello"
print("4.2.12 rjust() function:", hello.rjust(10, "#"))

'''
4.2.13 center() Centers the string
'''
hello = "hello"
print("4.2.13 center() function:", hello.center(15, "#"))

'''
4.3 Check
'''
'''
4.3.1 startswith() Checks if the string starts with a specified substring
    Returns True if yes, False otherwise
    string_sequence.startswith(substring, start_index, end_index)
'''
hello = "helloworld"
print("4.3.1 startswith():", hello.startswith("h"))

'''
4.3.2 endswith() Checks if the string ends with a specified substring
    Returns True if yes, False otherwise
'''
print("4.3.2 endswith():", hello.endswith("d"))

'''
4.3.3 isalpha() Checks if all characters are letters
    Returns True if yes, False otherwise
'''
hello = "hello"
print("4.3.3 isalpha() function:", hello.isalpha())

'''
4.3.4 isdigit() Checks if the string contains only digits
    Returns True if yes, False otherwise
'''
hello = "123"
print("4.3.4 isdigit() function:", hello.isdigit())

'''
4.3.5 isalnum() Checks if the string contains only letters or numbers
    Returns True if yes, False otherwise
'''
hello = "hello123"
print("4.3.5 isalnum() function:", hello.isalnum())

'''
4.3.6 isspace() Checks if the string contains only spaces
    Returns True if yes, False otherwise
'''
hello = "     "
print("4.3.6 isspace() function:", hello.isspace())
