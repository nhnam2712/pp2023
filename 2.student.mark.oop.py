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

    def __str__(self):
        return f"{self.name} ({self.id})"

# Define a subclass for courses that inherits from the base class
class Course(Record):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.marks = {}

    def __str__(self):
        return f"{self.name} ({self.id})"

    # Define a method to add a mark for a student
    def add_mark(self, student, mark):
        self.marks[student] = mark

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
    id = int(input("Enter student id: "))
    DOB = input("Enter student dob: ")
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

# Allow the user to input marks for each student in each course
for course in courses:
    print(f"Input marks for course {course}:")
    for student in students:
        mark = input(f"Enter mark for {student}: ")
        course.add_mark(student, mark)

# Print all student and course information, along with marks
print("Students:")
for student in students:
    print(student)

print("Courses:")
for course in courses:
    print(course)
    course.print_marks()
