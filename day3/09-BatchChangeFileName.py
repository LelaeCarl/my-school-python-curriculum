import os

# Step 1: Get the name of the file to back up
userFileName = input("Please enter the backup file name:")

# Step 2: Check if the file name includes a suffix (e.g., ".txt")
if userFileName.find(".") > 0:
    # Step 3: Get the name of the folder for backup files
    userDirName = input("Please enter the name of the folder you want to create:")

    # Step 4: Check if the folder exists
    if userDirName not in os.listdir():
        # Step 5: Create the folder if it does not exist
        os.mkdir(userDirName)
    # Step 6: Read the content of the original file
    with open(userFileName, 'r') as f:
        content = f.read()

    # Step 7: Switch to the specified folder
    os.chdir("./" + userDirName)

    # Step 8: Split the input file name into the name and extension
    oldList = userFileName.split(".")

    # Step 9: Create 10 backup files with the format `test-[备份]-01.txt` to `test-[备份]-10.txt`
    for i in range(1, 11):
        newFileName = oldList[0] + "-[backup]-%02d." % i + oldList[1]
        with open(newFileName, 'w') as newFile:
            newFile.write(content)

    # Step 10: Get the list of files in the folder
    dirList = os.listdir()

    # Step 11: Prepare the new file names by replacing `备份` with `大学`
    newDirList = [file.replace("backup", "university") for file in dirList]

    # Step 12: Rename all backup files to the new format
    for i in range(len(dirList)):
        os.rename(dirList[i], newDirList[i])

    print("All backup files have been successfully created and renamed!")
else:
    print("The file name is invalid, please make sure that the file name contains a suffix (for example:.txt)")
