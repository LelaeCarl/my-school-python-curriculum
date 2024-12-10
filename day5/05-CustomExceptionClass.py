'''
05 - Custom Exception Class
'''

class ShortInputException(Exception):
    def __init__(self, length, minLen):
        self.length = length  # Instance attribute
        self.minLen = minLen  # Instance attribute

    def __str__(self):
        return f"The length of the entered password is {self.length}, " \
               f"which cannot be less than {self.minLen}"

if __name__ == '__main__':
    try:
        con = input("Please enter a password: ")
        if len(con) < 3:
            raise ShortInputException(len(con), 3)
    except Exception as result:
        print(result)
    else:
        print("Password entry completed")
