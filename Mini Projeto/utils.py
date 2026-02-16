def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter student grade (0-10): "))
            if 0 <= grade <= 10:
                return grade
            print("Grade must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")
