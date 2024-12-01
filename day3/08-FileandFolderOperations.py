# 08 - File and Folder Operations

"""
This script demonstrates various file and folder operations using Python's `os` module.

Operations include:
1. Renaming a file
2. Deleting a file
3. Creating a new folder
4. Retrieving the current working directory
5. Changing the current working directory
6. Listing all files and folders in a directory
"""

import os

# Step 1: Rename a file
# Syntax: os.rename("current_file_name", "new_file_name")
# Uncomment the following line to rename "test-[备份].txt" to "test-[大学].txt"
# os.rename("test-[备份].txt", "test-[大学].txt")
# print("File renamed successfully.")

# Step 2: Delete a file
# Syntax: os.remove("file_name")
# Uncomment the following line to delete "test-[大学].txt"
# os.remove("test-[大学].txt")
# print("File deleted successfully.")

# Step 3: Create a folder
# Syntax: os.mkdir("folder_name")
# Uncomment the following line to create a folder named "江苏师范大学"
# os.mkdir("江苏师范大学")
# print("Folder created successfully.")

# Step 4: Get the current working directory
# Syntax: os.getcwd()
#current_dir = os.getcwd()
#print("4. Current working directory:", current_dir)

# Step 5: Change the current working directory
# Syntax: os.chdir("new_directory_path")
# Uncomment the following lines to change to the "江苏师范大学" directory
# os.chdir("./江苏师范大学")
# print("5. Changed current working directory:", os.getcwd())

# Step 6: List all files and folders in the current directory
# Syntax: os.listdir("directory_path")
# If no path is specified, it lists items in the current directory
directory_list = os.listdir()
print("6. List of files and folders in the current directory:", directory_list)
