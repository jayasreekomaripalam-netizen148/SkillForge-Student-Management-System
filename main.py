import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "students.json"


def load_students():
    DATA_DIR.mkdir(exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("{}", encoding="utf-8")

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student data.")
        return {}


def save_students(students):
    DATA_DIR.mkdir(exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(students, indent=4), encoding="utf-8"
    )


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("This student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    course = input("Enter course: ").strip()
    email = input("Enter email: ").strip()

    if not name or not course:
        print("Name and course are required.")
        return

    if age:
        try:
            if int(age) <= 0:
                print("Age must be a positive number.")
                return
        except ValueError:
            print("Age must be a valid number.")
            return

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- ALL STUDENTS ---")
    for student_id, details in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {details.get('name', '')}")
        print(f"Age: {details.get('age', '')}")
        print(f"Course: {details.get('course', '')}")
        print(f"Email: {details.get('email', '')}")


def search_student(students):
    query = input("Enter student ID or name: ").strip().lower()

    matches = [
        (student_id, details)
        for student_id, details in students.items()
        if query and (
            query in student_id.lower()
            or query in details.get("name", "").lower()
        )
    ]

    if not matches:
        print("No matching student found.")
        return

    for student_id, details in matches:
        print(f"\nID: {student_id}")
        for field, value in details.items():
            print(f"{field.title()}: {value}")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    details = students[student_id]
    print("Press Enter to keep the existing value.")

    for field in ("name", "age", "course", "email"):
        current = details.get(field, "")
        new_value = input(f"{field.title()} [{current}]: ").strip()

        if not new_value:
            continue

        if field == "age":
            try:
                if int(new_value) <= 0:
                    print("Age must be positive. Keeping old value.")
                    continue
            except ValueError:
                print("Invalid age. Keeping old value.")
                continue

        if field in ("name", "course") and not new_value:
            continue

        details[field] = new_value

    save_students(students)
    print("Student record updated!")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {students[student_id].get('name', student_id)}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        del students[student_id]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
