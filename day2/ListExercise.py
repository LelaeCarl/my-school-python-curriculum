# 05 - Dictionary Comprehensive Exercise

# Step 1: Define the studentList variable
student_list = []

# Step 2: Use a while loop to display menu options
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Modify Student")
    print("4. Remove Student")
    print("5. Exit System")

    # Step 3: Receive menu selection input
    choice = input("Enter your choice (1-5): ")

    # Step 4: Handle menu options
    if choice == "1":
        # Add Student
        student = {}
        student["name"] = input("Enter student's name: ")
        student["age"] = input("Enter student's age: ")
        student["gender"] = input("Enter student's gender: ")
        student["address"] = input("Enter student's address: ")
        student_list.append(student)
        print(f"Student added successfully: {student}")

    elif choice == "2":
        # Search Student
        if not student_list:
            print("No students found.")
        else:
            student_id = int(input("Enter the student ID to search (starting from 1): ")) - 1
            if 0 <= student_id < len(student_list):
                print(f"Student found: {student_list[student_id]}")
            else:
                print("Student ID not found.")

    elif choice == "3":
        # Modify Student
        if not student_list:
            print("No students available to modify.")
        else:
            student_id = int(input("Enter the student ID to modify (starting from 1): ")) - 1
            if 0 <= student_id < len(student_list):
                student = student_list[student_id]
                print(f"Current student details: {student}")
                student["name"] = input("Enter new name (leave blank to keep current): ") or student["name"]
                student["age"] = input("Enter new age (leave blank to keep current): ") or student["age"]
                student["gender"] = input("Enter new gender (leave blank to keep current): ") or student["gender"]
                student["address"] = input("Enter new address (leave blank to keep current): ") or student["address"]
                print("Student details updated successfully.")
            else:
                print("Student ID not found.")

    elif choice == "4":
        # Remove Student
        if not student_list:
            print("No students available to remove.")
        else:
            student_id = int(input("Enter the student ID to remove (starting from 1): ")) - 1
            if 0 <= student_id < len(student_list):
                removed_student = student_list.pop(student_id)
                print(f"Student removed successfully: {removed_student}")
            else:
                print("Student ID not found.")

    elif choice == "5":
        # Exit System
        print("Exiting the system. Goodbye!")
        break

    else:
        # Invalid input
        print("Invalid choice. Please enter a number between 1 and 5.")
