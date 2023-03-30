# Define a class for Student
class Student:
    def __init__(self, name, id, dob):
        self._name = name
        self._id = id
        self._dob = dob

    # Define getter methods for the name, id, and dob attributes
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_dob(self):
        return self._dob

    # Define setter methods for the name, id, and dob attributes
    def set_name(self, name):
        self._name = name

    def set_id(self, id):
        self._id = id

    def set_dob(self, dob):
        self._dob = dob


# Define a class for Course
class Course:
    def __init__(self, name, id):
        self._name = name
        self._id = id
        self._marks = {}

    # Define getter methods for the name and id attributes
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    # Define a method to input marks for a student
    def input_mark(self, student, mark):
        self._marks[student.get_id()] = mark

    # Define a method to show marks for all students in the course
    def show_marks(self):
        for student_id, mark in self._marks.items():
            print(f"Student {student_id} has mark {mark} in {self._name}")


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

# Allow the user to input marks for all students in all courses
for course in courses:
    print(f"Input marks for course {course.get_name()}")
    for student in students:
        mark = input(f"* Student {student.get_name()}: ")
        course.input_mark(student, mark)

# Print all student records
print("listing students")
for student in students:
    print(student.get_name(), student.get_id(), student.get_dob())

# Print all course records
print("listing courses")
for course in courses:
    print(course.get_name(), course.get_id())

# Show marks for all students in all courses
print("show marks")
for course in courses:
    course.show_marks()