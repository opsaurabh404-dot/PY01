# student_management_system.py
# Simple Student Management System with Menu

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    try:
        marks = float(marks)
        students[name] = marks
        print(f"{name} added successfully!\n")
    except ValueError:
        print("Invalid marks! Please enter a number.\n")

def view_students():
    if not students:
        print("No students added yet.\n")
    else:
        print("All Students:")
        for name, marks in students.items():
            print(f"{name}: {marks}")
        print()

def update_marks():
    name = input("Enter student name to update: ")
    if name in students:
        marks = input("Enter new marks: ")
        try:
            marks = float(marks)
            students[name] = marks
            print(f"{name}'s marks updated successfully!\n")
        except ValueError:
            print("Invalid marks! Please enter a number.\n")
    else:
        print(f"No student found with name {name}\n")

def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
