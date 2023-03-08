#create class for students and courses
class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.mark = {}

#define marks
    def input_mark(self, students):
        print(f"Input mark for course {self.name}")
        for student in students:
            mark = input(f"* Student {student.name}: ")
            self.mark[student.id] = mark

    def show_mark(self):
        for student_id, mark in self.mark.items():
            print(f"Student {student_id} has mark {mark}")

#create dict for students and courses
students = []
courses = []

while True:
    name = input("Enter student name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter student id: "))
    dob = input("Enter student dob: ")
    students.append(Student(name, id, dob))

while True:
    name = input("Enter course name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter course id: "))
    courses.append(Course(name, id))

for course in courses:
    course.input_mark(students)

print("listing students")
for student in students:
    print(student.name, student.id, student.dob)

print("listing courses")
for course in courses:
    print(course.name, course.id)

print("show mark:")
for course in courses:
    course.show_mark()
