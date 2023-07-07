database = {
    "students": [
        {"first_name": "John", "last_name": "Smith", "class": "3C"},
        {"first_name": "Anna", "last_name": "Purple", "class": "3C"},
        {"first_name": "Jan", "last_name": "Kowalski", "class": "4E"}
    ],
    "teacher": [
        {"first_name": "Mehmet", "last_name": "Simsek", "subject": "math", "classes": ["3C", "4E"]}
    ],
    "homeroom_teacher": [
        {"first_name": "Ahmet", "last_name": "Hakim", "class": "4E"}
    ]
}

def create(user_type):
    if user_type == "student":
        student_first_name = input("Provide the student's first name: ")
        student_last_name = input("Provide the student's last name: ")
        student_class = input("Provide the student's class: ")
        new_student = {
            "first_name": student_first_name,
            "last_name": student_last_name,
            "class": student_class
        }
        database["students"].append(new_student)

    elif user_type == "teacher":
        teacher_first_name = input("Provide the teacher's first name: ")
        teacher_last_name = input("Provide the teacher's last name: ")
        teacher_classes = input("Provide the teacher's classes (comma-separated): ")
        teacher_classes_list = [class_name.strip() for class_name in teacher_classes.split(",")]
        new_teacher = {
            "first_name": teacher_first_name,
            "last_name": teacher_last_name,
            "classes": teacher_classes_list
        }
        database["teacher"].append(new_teacher)

    elif user_type == "homeroom teacher":
        homeroom_teacher_first_name = input("Provide the homeroom teacher's first name: ")
        homeroom_teacher_last_name = input("Provide the homeroom teacher's last name: ")
        homeroom_teacher_class = input("Provide the homeroom teacher's class: ")
        new_homeroom_teacher = {
            "first_name": homeroom_teacher_first_name,
            "last_name": homeroom_teacher_last_name,
            "class": homeroom_teacher_class
        }
        database["homeroom_teacher"].append(new_homeroom_teacher)


def manage(user_type):
    if user_type == "student":
        first_name = input("Provide student's first name: ")
        last_name = input("Provide student's last name: ")
        found = False
        for student in database["students"]:
            if student["first_name"] == first_name and student["last_name"] == last_name:
                print(f"{first_name} {last_name} attends the following classes:")
                for teacher in database["teacher"]:
                    if student["class"] in teacher["classes"]:
                        print(f"- Class: {student['class']}, Teacher: {teacher['first_name']} {teacher['last_name']}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif user_type == "homeroom teacher":
        first_name = input("Provide homeroom teacher's first name: ")
        last_name = input("Provide homeroom teacher's last name: ")
        found = False
        for homeroom_teacher in database["homeroom_teacher"]:
            if homeroom_teacher["first_name"] == first_name and homeroom_teacher["last_name"] == last_name:
                print(f"Homeroom teacher {first_name} {last_name} leads class {homeroom_teacher['class']}")
                print("Student list:")
                for student in database["students"]:
                    if student["class"] == homeroom_teacher["class"]:
                        print(f"- {student['first_name']} {student['last_name']}")
                found = True
                break
        if not found:
            print("Homeroom teacher not found.")

    elif user_type == "teacher":
        teacher_first_name = input("Provide teacher's first name: ")
        teacher_last_name = input("Provide teacher's last name: ")
        found = False
        for teacher in database["teacher"]:
            if teacher["first_name"] == teacher_first_name and teacher["last_name"] == teacher_last_name:
                print(f"Teacher {teacher_first_name} {teacher_last_name} teaches the following classes:")
                for class_name in teacher["classes"]:
                    print(f"- {class_name}")
                found = True
                break
        if not found:
            print("Teacher not found.")

    elif user_type == "class":
        class_choice = input("Provide class: ")
        found = False
        for student in database["students"]:
            if student["class"] == class_choice:
                print(f"Students in class {class_choice}:")
                print(f"- {student['first_name']} {student['last_name']}")
                found = True

        for homeroom_teacher in database["homeroom_teacher"]:
            if homeroom_teacher["class"] == class_choice:
                print(f"Homeroom teacher: {homeroom_teacher['first_name']} {homeroom_teacher['last_name']}")
                found = True

        if not found:
            print("No students or homeroom teacher found in the specified class.")


while True:
    option = input("Provide option ('create', 'manage', 'end'): ")

    if option == "create":
        create_option = input("Provide user type for create ('student', 'teacher', 'homeroom teacher'): ")
        create(create_option)
    elif option == "manage":
        manage_user_type = input("Provide user type for manage ('class', 'student', 'teacher', 'homeroom teacher'): ")
        manage(manage_user_type)
    elif option == "end":
        break
    elif option == "database":
        print(database)