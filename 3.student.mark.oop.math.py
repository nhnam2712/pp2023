#create import
import math

#create class for students and courses
class Student:
    def __init__(self, name, id, dob):
        self.__name = 0
        self.__id = 0
        self.__dob = 0

    def _get_name(self):
            return self.__name

    def set_name(self, name):
            self.__name = name

    def _get_id(self):
            return self.__id

    def set_id(self, id):
            self.__id = id

    def _get_dob(self):
            return self.__dob

    def set_dob(self, dob):
            self.__dob = dob



class Course:
    def __init__(self, name, id):
        self.__name = 0
        self.__id = 0
        self.__mark = {}

    def _get_name(self):
            return self.__name

    def set_name(self, name):
            self.__name = name

    def _get_id(self):
            return self.__id

    def set_id(self, id):
            self.__id = id

    def _get_mark(self):
            return self.__mark

    def set_mark(self, mark):
            self.__mark = mark

#define marks
    def input_mark(self, students):
        print(f"Input mark for course {self.__name}")
        for student in students:
            mark = float(input(f"* Student {student.__name}: "))
            self.__mark[student._get_id_()] = math.floor(mark*10)/10  #round-down to 1 digit

    def show_mark(self):
        for student_id, mark in self.__mark.items():
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
    print(student._get_name(), student._get_id(), student._get_dob())

print("listing courses")
for course in courses:
    print(course._get_name(), course._get_id())

print("show mark:")
for course in courses:
    course.show_mark()
