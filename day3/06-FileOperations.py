# 06 - File Operations

"""
1. Purpose of File Operations
   - Read content
   - Write content
   - Backup content
"""

"""
2. Basic File Operations
"""

# 2.1 File Operation Steps
# 2.1.1 Open the file using open(name, mode)
# name: Target file name as a string (including the path)
# mode: Specifies how the file is accessed (read-only, write, append, etc.)

"""
2.1.2 File Opening Modes
    r       Open a file for reading. File pointer is at the beginning. Default mode.
    rb      Open a file in binary format for reading. Pointer at the beginning.
    r+      Open a file for reading and writing. Pointer at the beginning.
    rb+     Open a binary file for reading and writing. Pointer at the beginning.
    w       Open a file for writing. Overwrites if file exists; creates a new file if it doesn't.
    wb      Open a binary file for writing. Overwrites if file exists; creates a new file if it doesn't.
    w+      Open a file for reading and writing. Overwrites if file exists; creates a new file if it doesn't.
    wb+     Open a binary file for reading and writing. Overwrites if file exists; creates a new file if it doesn't.
    a       Open a file for appending. Pointer at the end if file exists; creates a new file if it doesn't.
    ab      Open a binary file for appending. Pointer at the end if file exists; creates a new file if it doesn't.
    a+      Open a file for reading and appending. Pointer at the end if file exists; creates a new file if it doesn't.
    ab+     Open a binary file for reading and appending. Pointer at the end if file exists; creates a new file if it doesn't.

    - r: Read
    - w: Write
    - +: Read and Write
    - b: Binary Mode
"""

# 2.1.3 File Object Methods

# Writing to a file
f = open("test.txt", 'w')
f.write("I'm so so so sorryyy\nI didn't mean to break your heart :(")
f.close()

# Reading the entire content of a file using read()
f = open("test.txt", 'r')
content = f.read()
f.close()
print("read() function:", content)

# Reading all lines into a list using readlines()
f = open("test.txt", 'r')
content = f.readlines()
f.close()
print("readlines() function:", content)

# Reading one line at a time using readline()
f = open("test.txt", 'r')
line1 = f.readline()
print("First line:", line1)
line2 = f.readline()
print("Second line:", line2)
f.close()

"""
seek(): Move the file pointer
   - Syntax: file_object.seek(offset, whence)
   - whence:
     0: From the beginning of the file
     1: From the current position
     2: From the end of the file
"""

f = open("test.txt", 'rb')

# Example content in file: "World123-01!!!"

# Move 5 bytes from the beginning of the file
f.seek(5, 0)
content1 = f.readline()
print("Pointer moved 5 bytes from the start:", content1)

# Move 10 bytes forward from the current position
f.seek(10, 1)
content2 = f.readline()
print("Pointer moved 10 bytes forward from current position:", content2)

# Move 10 bytes backward from the current position
f.seek(-10, 1)
content3 = f.readline()
print("Pointer moved 10 bytes backward from current position:", content3)

# Move 10 bytes backward from the end of the file
f.seek(-10, 2)
content4 = f.readline()
print("Pointer moved 10 bytes backward from the end:", content4)

f.close()
