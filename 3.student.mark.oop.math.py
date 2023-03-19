import math

# Define a base class for both students and courses
class Record:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Define a subclass for students that inherits from the base class
class Student(Record):
    def __init__(self, name, id, DOB):
        super().__init__(name, id)
        self.DOB = DOB
        self.courses = {}

    def __str__(self):
        return f"{self.name} ({self.id})"

    def add_course(self, course):
        self.courses[course] = 0

    def add_grade(self, course, grade):
        self.courses[course] = grade

#calculate the gpa but the scale is 10 points
    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0
        for course, grade in self.courses.items():
            credits = course.credit
            if grade == "A":
                grade_points = 4.0
            elif grade == "A-":
                grade_points = 3.7
            elif grade == "B+":
                grade_points = 3.3
            elif grade == "B":
                grade_points = 3.0
            elif grade == "B-":
                grade_points = 2.7
            elif grade == "C+":
                grade_points = 2.3
            elif grade == "C":
                grade_points = 2.0
            elif grade == "C-":
                grade_points = 1.7
            elif grade == "D+":
                grade_points = 1.3
            elif grade == "D":
                grade_points = 1.0
            else:
                grade_points = 0.0
            total_credits += credits
            total_grade_points += grade_points * credits
        if total_credits == 0:
            return 0
        else:
            return total_grade_points / total_credits

# Define a subclass for courses that inherits from the base class
class Course(Record):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.marks = {}
        self.credit = {}

    def __str__(self):
        return f"{self.name} ({self.id})"

    # Defind a method to add a credit for a course
    def add_credit(self, course, credit):
        self.credit[course] = credit

    # Defind a method to print a credit for a course
    def print_credit(self):
        for course, credit in self.credit.items():
            print(f"{course}: {credit} credits")

    # Define a method to add a mark for a student
    def add_mark(self, student, mark):
        self.marks[student] = math.floor(float(mark)*10)/10

    # Define a method to print all marks for the course
    def print_marks(self):
        for student, mark in self.marks.items():
            print(f"{student}: {mark}")

# Create empty lists for students and courses
students = []
courses = []

# Allow the user to input student information
while True:
    name = input("Enter student name (or 'done' to exit): ")
    if name == "done":
        break
    id = str(input("Enter student id: "))
    DOB = str(input("Enter student dob: "))
    student = Student(name, id, DOB)
    students.append(student)

# Allow the user to input course information
while True:
    name = input("Enter course name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter course id: "))
    course = Course(name, id)
    courses.append(course)

#Allow the user to input credit for each student in each course
for course in courses:
    print(f"Input credit for course {course}:")
    credit = input(f"Enter credit for {course}: ")
    course.add_credit(course, credit)

# Allow the user to input marks for each student in each course
for course in courses:
    print(f"Input marks for course {course}:")
    for student in students:
        mark = input(f"Enter mark for {student}: ")
        course.add_mark(student, mark)

# Calculate and print GPA for each student
for student in students:
    gpa = student.calculate_gpa()
    print(f"{student}: GPA = {gpa:.2f}")

# Print all student and course information, along with marks
print("Students:")
for student in students:
    print(student)

print("Courses:")
for course in courses:
    print(course)
    course.print_credit()
    course.print_marks()