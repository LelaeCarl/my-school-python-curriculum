'''
生管理系统
需求如下:
1.定义studentList的列表变量
2.使用while死循环 输出菜单选项
    1.添加学生
    2.查询学生
    3.修改学生
    4.删除学生
    5.退出系统
3.使用input函数接收控制台输入的序号1,2,3,4,5
4.根据输入的序号判断菜单选项, 如果不是以上5个数字则输出 错了
5.若添加学生 定义字典student 生成学生信息 name,age,sex,address
将字典变量 天极爱studentList中
6.所有的功能都使用函数处理
'''

# Initialize an empty list to store student information
student_list = []


def display_menu():
    """
    Display the menu options.
    """
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Modify Student")
    print("4. Delete Student")
    print("5. Exit System")


def add_student():
    """
    Add a new student to the list.
    """
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    sex = input("Enter student gender: ")
    address = input("Enter student address: ")

    student = {
        "name": name,
        "age": age,
        "sex": sex,
        "address": address
    }

    student_list.append(student)
    print("Student has been added successfully!")


def view_students():
    """
    View all students in the list.
    """
    if not student_list:
        print("No students found!")
        return

    for index, student in enumerate(student_list):
        print(
            f"{index + 1}. Name: {student['name']}, Age: {student['age']}, Gender: {student['sex']}, Address: {student['address']}")


def modify_student():
    """
    Modify a student's information.
    """
    view_students()
    if not student_list:
        return

    try:
        student_index = int(input("Enter the student number to modify: ")) - 1
        if 0 <= student_index < len(student_list):
            print(f"Current Info: {student_list[student_index]}")
            name = input("Enter new name (leave blank to keep unchanged): ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            sex = input("Enter new gender (leave blank to keep unchanged): ")
            address = input("Enter new address (leave blank to keep unchanged): ")

            if name:
                student_list[student_index]['name'] = name
            if age:
                student_list[student_index]['age'] = age
            if sex:
                student_list[student_index]['sex'] = sex
            if address:
                student_list[student_index]['address'] = address

            print("Student information has been updated!")
        else:
            print("Invalid student number!")
    except ValueError:
        print("Please enter a valid number!")


def delete_student():
    """
    Delete a student from the list.
    """
    view_students()
    if not student_list:
        return

    try:
        student_index = int(input("Enter the student number to delete: ")) - 1
        if 0 <= student_index < len(student_list):
            removed_student = student_list.pop(student_index)
            print(f"Student {removed_student['name']} has been deleted.")
        else:
            print("Invalid student number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    """
    Main function to run the student management system.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


# Run the main function
if __name__ == "__main__":
    main()
