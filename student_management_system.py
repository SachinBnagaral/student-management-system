
#Student Management System
"""
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save & Exit
Enter your choice:
Details of each student to be stored:
- ID
- Name
- Age
- Course
- Marks
"""
#creating data structure --> lists 
#intialize empty list
# Student Management System

# ===== Student Management System =====

students = []   # list to store student records

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")
    students.append([sid, name, age, course, marks])
    print("Student added successfully.\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    print("\nID | Name | Age | Course | Marks")
    print("-" * 35)
    for s in students:
        print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]}")
    print()

def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s[0] == sid:
            print("Student Found:", s, "\n")
            return
    print("Student not found.\n")

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s[0] == sid:
            s[1] = input("Enter New Name: ")
            s[2] = input("Enter New Age: ")
            s[3] = input("Enter New Course: ")
            s[4] = input("Enter New Marks: ")
            print("Student updated successfully.\n")
            return
    print("Student not found.\n")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s[0] == sid:
            students.remove(s)
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")
