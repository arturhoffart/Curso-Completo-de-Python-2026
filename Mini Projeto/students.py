def create_student(name, grade):
    return {
        "name": name,
        "grade": grade
    }


def add_student(student_list, student):
    student_list.append(student)


def search_student(student_list, name):
    for student in student_list:
        if student["name"].lower() == name.lower():
            return student
    return None


def calculate_average(student_list):
    if not student_list:
        return 0

    total = sum(student["grade"] for student in student_list)
    return total / len(student_list)


def generate_report(student_list):
    if not student_list:
        return "No students registered."

    report_lines = []
    for student in student_list:
        report_lines.append(f"Name: {student['name']} | Grade: {student['grade']}")

    average = calculate_average(student_list)
    highest = max(student_list, key=lambda x: x["grade"])
    lowest = min(student_list, key=lambda x: x["grade"])

    report_lines.append(f"\nClass average: {average:.2f}")
    report_lines.append(f"Highest grade: {highest['name']} ({highest['grade']})")
    report_lines.append(f"Lowest grade: {lowest['name']} ({lowest['grade']})")

    return "\n".join(report_lines)
