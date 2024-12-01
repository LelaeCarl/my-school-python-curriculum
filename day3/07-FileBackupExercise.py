# 07 - File Backup Practice

"""
Requirements:
1. Use the input() function to input the name of the file to back up, e.g., 'test.txt'.
2. Create a backup of the input file.
3. The backup file name should be in the format: 'test-[备份].txt'.
   - The file name needs to be dynamically modified based on the user's input.
"""

# Step 1: Input the name of the file to back up
userFileName = input("Please enter the name of the file to back up: ")

# Step 2: Split the file name into name and extension, e.g., ['test', 'txt']
fileNameList = userFileName.split(".")
if len(fileNameList) != 2:  # Ensure the input has a valid file format
    print("Invalid file name. Please provide a valid file with an extension (e.g., 'test.txt').")
else:
    # Step 3: Construct the new backup file name
    newFileName = fileNameList[0] + '-[backup].' + fileNameList[1]

    try:
        # Step 4: Open the original file and read its contents
        with open(userFileName, 'r') as f:
            content = f.read()  # Read all the file content as a string

        # Step 5: Open the backup file and write the content into it
        with open(newFileName, 'w') as newFile:
            newFile.write(content)

        print(f"Backup created successfully! New file name: {newFileName}")
    except FileNotFoundError:
        print(f"Error: The file '{userFileName}' does not exist. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
