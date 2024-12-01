# 05-Student Dictionary Practice
# Requirements:
# 1. Define a list variable `studentList`
# 2. Use an infinite `while` loop to display menu options:
#    1. Add Student
#    2. Query Students
#    3. Edit Student
#    4. Delete Student
#    5. Exit System
# 3. Use `input` to receive console input (1, 2, 3, 4, 5)
# 4. Based on the input number, perform the corresponding menu action. If the input is not one of these five, print an error message.
# 5. When adding a student, define a dictionary `student` to store student details: name, age, gender, and address.
#    Append this dictionary to the `studentList`.
# 6. Other functionalities are implemented similarly.

# 1. Define the student information list
studentList = []

# 2. Infinite loop
while True:
    # 2.1 Menu options
    print("1. Add Student\n2. Query Students\n3. Edit Student\n4. Delete Student\n5. Exit System")
    # 2.2 Prompt the user to input a selection number
    num = int(input("Please enter your choice: "))
    # 2.3 Conditional statements
    if num == 1:
        # Create a new dictionary
        student = {}
        student['name'] = input("Name: ")
        student['age'] = input("Age: ")
        student['sex'] = input("Gender: ")
        student['address'] = input("Address: ")
        # Add the dictionary to the list
        studentList.append(student)
    elif num == 2:
        # Loop through and display student information
        for index, stu in enumerate(studentList):
            print(f"{index} => {stu['name']}, {stu['age']}, {stu['sex']}, {stu['address']}")
    elif num == 3:
        # Display current student information
        for index, stu in enumerate(studentList):
            print(f"{index} => {stu['name']}, {stu['age']}, {stu['sex']}, {stu['address']}")
        # Input the index of the student to be edited
        num = int(input("Enter the index of the student to edit: "))
        # Input new student information
        student = {}
        student['name'] = input("Name: ")
        student['age'] = input("Age: ")
        student['sex'] = input("Gender: ")
        student['address'] = input("Address: ")
        # Overwrite the existing student information
        studentList[num] = student
    elif num == 4:
        # Display current student information
        for index, stu in enumerate(studentList):
            print(f"{index} => {stu['name']}, {stu['age']}, {stu['sex']}, {stu['address']}")
        # Input the index of the student to be deleted
        num = int(input("Enter the index of the student to delete: "))
        # Delete the student based on the index
        del studentList[num]
    elif num == 5:
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("Invalid input, please try again.")
