'''
07 - Student Management System - Complete Version
Requirements:
1. Create a class containing various operation functions.
2. Use student.txt to store and retrieve data:
   - Example (Simple): 张三:18:男:上海路101号
   - Example (Complex): name:张三, age:18, sex:男, address:上海路101号
3. Validate different data values:
   - num must include digits. For example, 18 includes digits and meets the conditions.
4. Create a data list studentList to store the data.
5. Record a video demonstration and send it to the group.
'''

import os

class Student:
    def __init__(self, name, age, sex, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

    def __str__(self):
        return f"{self.name}:{self.age}:{self.sex}:{self.address}"

    def to_dict(self):
        return {"name": self.name, "age": self.age, "sex": self.sex, "address": self.address}


class StudentManagementSystem:
    def __init__(self, filename="student.txt"):
        self.filename = filename
        self.studentList = []
        self.load_data()

    def load_data(self):
        """Load data from the student.txt file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(":")
                        if len(parts) == 4:  # Simple format
                            name, age, sex, address = parts
                            self.studentList.append(Student(name, age, sex, address))
                        else:  # Complex format
                            data = {}
                            for item in line.split(","):
                                key, value = item.split(":")
                                data[key.strip()] = value.strip()
                            self.studentList.append(Student(data["name"], data["age"], data["sex"], data["address"]))

    def save_data(self):
        """Save data to the student.txt file."""
        with open(self.filename, "w", encoding="utf-8") as file:
            for student in self.studentList:
                file.write(str(student) + "\n")

    def add_student(self, name, age, sex, address):
        """Add a new student."""
        if not age.isdigit():
            print("Error: Age must be numeric!")
            return
        self.studentList.append(Student(name, age, sex, address))
        self.save_data()
        print(f"Student {name} added successfully!")

    def view_students(self):
        """View all students."""
        if not self.studentList:
            print("No students available.")
        else:
            for idx, student in enumerate(self.studentList, start=1):
                print(f"{idx}. {student}")

    def search_student(self, name):
        """Search for a student by name."""
        results = [student for student in self.studentList if student.name == name]
        if results:
            for student in results:
                print(student)
        else:
            print(f"No student found with the name '{name}'.")

    def delete_student(self, name):
        """Delete a student by name."""
        self.studentList = [student for student in self.studentList if student.name != name]
        self.save_data()
        print(f"Student {name} deleted successfully!")

    def update_student(self, name, age=None, sex=None, address=None):
        """Update a student's details."""
        for student in self.studentList:
            if student.name == name:
                if age:
                    if age.isdigit():
                        student.age = age
                    else:
                        print("Error: Age must be numeric!")
                        return
                if sex:
                    student.sex = sex
                if address:
                    student.address = address
                self.save_data()
                print(f"Student {name} updated successfully!")
                return
        print(f"No student found with the name '{name}'.")


# Main program
if __name__ == "__main__":
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            sex = input("Enter sex: ")
            address = input("Enter address: ")
            system.add_student(name, age, sex, address)
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            name = input("Enter name to search: ")
            system.search_student(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            system.delete_student(name)
        elif choice == "5":
            name = input("Enter name to update: ")
            age = input("Enter new age (leave blank to keep current): ")
            sex = input("Enter new sex (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            system.update_student(name, age if age else None, sex if sex else None, address if address else None)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
            