#import sections
import math

# Define a class for Student
class Student:
    def __init__(self, name, id, dob):
        self._name = name
        self._id = id
        self._dob = dob
        self._gpa = 0.0

    # Define getter methods for the name, id, and dob attributes
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_dob(self):
        return self._dob

    def get_gpa(self):
        return self._gpa


    # Define setter methods for the name, id, and dob attributes
    def set_name(self, name):
        self._name = name

    def set_id(self, id):
        self._id = id

    def set_dob(self, dob):
        self._dob = dob

    def set_gpa(self, gpa):
        self._gpa = gpa

# Define a method to calculate the GPA based on the marks obtained in each course
    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        for course in courses:
            if self._id in course.get_marks():
                mark = course.get_marks()[self._id]
                credit = course.get_credits()
                total_credits += credit
                weighted_sum += mark * credit
        if total_credits > 0:
            self._gpa = weighted_sum / total_credits

        return self._gpa

# Define a class for Course
class Course:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._marks = {}
        self._credits = 0

    # Define getter methods for the name and id attributes
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_marks(self):
        return self._marks

    def get_credits(self):
        return self._credits

    # Define a method to input marks for a student
    def input_mark(self, student, mark):
        self._marks[student.get_id()] = float(mark)
    # Define a method to show marks for all students in the course
    def show_marks(self):
        for student_id, mark in self._marks.items():
            print(f"Student {student_id} has mark {mark} in {self._name}")

    def input_credit(self, credit):
        self._credits = credit

    def show_credits(self):
        print(f"Course {self._name} has {self._credits} credits")


# Create empty lists for students and courses
students = []
courses = []

# Allow the user to input student information
while True:
    name = input("Enter student name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter student id: "))
    dob = input("Enter student dob: ")
    student = Student(name, id, dob)
    students.append(student)

# Allow the user to input course information
while True:
    name = input("Enter course name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter course id: "))
    course = Course(name, id)
    courses.append(course)

# Allow the user to input credits for all courses
for course in courses:
    print(f"Input credits for course {course.get_name()}")
    credit =int(input(f"* Course {course.get_name()}: "))
    course.input_credit(credit)

# Allow the user to input marks for all students in all courses
for course in courses:
    print(f"Input marks for course {course.get_name()}")
    for student in students:
        mark = int(input(f"* Student {student.get_name()}: "))
        course.input_mark(student, mark)

# Print all student records
print("listing students")
for student in students:
    print(f"Name: {student.get_name()}, ID: {student.get_id()}, DOB: {student.get_dob()}")

# Calculate and show GPA for each student
for student in students:
    gpa = student.calculate_gpa(courses)
    print(f"{student.get_name()} has {gpa} gpa")

# Sort students by GPA in descending order
sorted_students = sorted(students, key=lambda student: student.get_gpa(), reverse=True)

# Print sorted student records
print("Listing students (sorted by GPA)")
for student in sorted_students:
    print(student.get_name(), student.get_id(), student.get_dob(), student.get_gpa())

# Print all course records
print("listing courses")
for course in courses:
    print(course.get_name(), course.get_id())

# Show credits for all courses
print("show credits")
for course in courses:
    course.show_credits()

# Show marks for all students in all courses
print("show marks")
for course in courses:
    course.show_marks()