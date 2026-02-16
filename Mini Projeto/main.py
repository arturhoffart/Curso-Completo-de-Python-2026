from students import (
    create_student,
    add_student,
    search_student,
    generate_report
)

from utils import get_valid_name, get_valid_grade


def show_menu():
    print("\n=== Student Management System ===")
    print("1 - Add student")
    print("2 - Search student")
    print("3 - Show report")
    print("4 - Exit")


def main():
    student_list = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = get_valid_name()
            grade = get_valid_grade()
            student = create_student(name, grade)
            add_student(student_list, student)
            print("Student added successfully.")

        elif choice == "2":
            name = get_valid_name()
            student = search_student(student_list, name)
            if student:
                print(f"Found: Name: {student['name']} | Grade: {student['grade']}")
            else:
                print("Student not found.")

        elif choice == "3":
            report = generate_report(student_list)
            print("\n=== Report ===")
            print(report)

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
