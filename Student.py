import json
import os


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = []

    def add_grade(self, course_name, grade):
        if course_name not in self.courses:
            self.courses[course_name] = []

        self.courses[course_name].append(grade)

    def average(self):
        grades = []

        for course in self.courses.values():
            grades.extend(course)

        if len(grades) == 0:
            return 0

        return round(sum(grades) / len(grades), 2)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "courses": self.courses
        }


class StudentManager:
    def __init__(self):
        self.file_name = "students.json"
        self.students = {}
        self.load()

    def load(self):
        if not os.path.exists(self.file_name):
            return

        with open(self.file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                student = Student(
                    item["student_id"],
                    item["name"]
                )

                student.courses = item["courses"]

                self.students[student.student_id] = student

    def save(self):
        data = []

        for student in self.students.values():
            data.append(student.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_student(self):
        student_id = input("ID: ")
        name = input("Name: ")

        if student_id in self.students:
            print("Student already exists")
            return

        self.students[student_id] = Student(student_id, name)

        self.save()

        print("Student added")

    def show_students(self):
        if len(self.students) == 0:
            print("No students found")
            return

        for student in self.students.values():
            print("-" * 40)
            print(f"ID      : {student.student_id}")
            print(f"Name    : {student.name}")
            print(f"Average : {student.average()}")

    def add_course(self):
        student_id = input("Student ID: ")

        if student_id not in self.students:
            print("Student not found")
            return

        course = input("Course Name: ")

        self.students[student_id].add_course(course)

        self.save()

        print("Course added")

    def add_grade(self):
        student_id = input("Student ID: ")

        if student_id not in self.students:
            print("Student not found")
            return

        course = input("Course Name: ")

        try:
            grade = float(input("Grade: "))
        except:
            print("Invalid grade")
            return

        self.students[student_id].add_grade(course, grade)

        self.save()

        print("Grade added")

    def student_report(self):
        student_id = input("Student ID: ")

        if student_id not in self.students:
            print("Student not found")
            return

        student = self.students[student_id]

        print("\nStudent Report")
        print("-" * 40)
        print("Name:", student.name)
        print("ID:", student.student_id)

        for course, grades in student.courses.items():
            print(f"{course}: {grades}")

        print("Average:", student.average())


def menu():
    manager = StudentManager()

    while True:
        print("\nSMART STUDENT ASSISTANT")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Add Course")
        print("4. Add Grade")
        print("5. Student Report")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            manager.add_course()

        elif choice == "4":
            manager.add_grade()

        elif choice == "5":
            manager.student_report()

        elif choice == "0":
            break

        else:
            print("Invalid choice")


menu()
