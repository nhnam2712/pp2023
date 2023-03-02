# Create an empty list
students = []

# Define a function
def add_student(name, id, DOB):
    student = {'name': name, 'id': id, 'DOB': DOB}
    students.append(student)

# Define a function to print all student records
def print_students():
    for student in students:
        print(student['name'], student['id'], student['DOB'])

# Allow the user to input student information
while True:
    name = input("Enter student name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter student id: "))
    DOB = input("Enter student dob: ")
    add_student(name, id, DOB)

# Print all student records
print("listing students")
print_students()

# Create an empty list
courses = []

# Define a function
def add_courses(course_name, course_id):
    course = {'name': course_name, 'id': course_id}
    courses.append(course)

# Define a function to print all courses
def print_courses():
    for course in courses:
        print(course['name'], course['id'])


# Allow the user to input courses information
while True:
    name = input("Enter course name (or 'done' to exit): ")
    if name == "done":
        break
    id = int(input("Enter course id: "))
    add_courses(name, id)

#print all course records
print("listing courses")
print_courses()

#create empty list
marks = []

#define function to input mark
def input_mark(course, students):
    print(f"Input mark for course {course['name']}")
    course['mark'] = {}
    for student in students:
        mark = input(f"* Student {student['name']}: ")
        course['mark'][student['id']] = mark

for course in courses:
    input_mark(course,students)

#listing mark function
def show_mark(course):
    for (student_id, mark) in course['mark'].items():
        print(f"Student {student_id} has mark {mark}")

print("show mark:")
for course in courses:
    show_mark(course)