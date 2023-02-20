#define students infomation
students = {}
def input_students():
    num_students = int(input("enter a number of students: "))
    print("you have " + str(num_students) + " students")
    for i in range(num_students):
        student_id = input("enter id of student: ")
        student_name = input("enter full name of student: ")
        DOB =  input("enter Date of birth of student: ")
        students[student_id] = {'Name': student_name, 'DOB': DOB}

#define course infomation
courses = {}
def input_courses():
    num_courses = int(input("enter number of course: "))
    print("you have " + str(num_courses) + " course")
    for i in range(num_courses):
        course_id = input("enter id of course: ")
        course_name = input("enter name of course: ")
        courses[course_id] = {'Course Name': course_name}

#function input mark for student
marks = {}
def input_mark():
    course_id = input("enter your course id: ")
    if course_id not in courses:
        print("id is not correct!")
        return
    for student_id in students:
        mark = int(input(f"Enter the mark for{students[student_id]['Name']}: "))
        if student_id not in marks:
            marks[student_id] = {}
        marks[student_id][course_id] = mark

#list courses
def list_courses():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['Name']}")

#list students
def list_students():
    for student_id in students:
        print(f"{student_id}: {students[student_id]['Name']}")

#show marks for given course
def show_mark():
    course_id = input("enter your course id: ")
    if course_id not in courses:
        print("id is not correct!")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['Name']}: {marks[student_id][course_id]}")
        else:
            print(f"{students[student_id]['Name']}: N/A")

#Main
input_students()
input_courses()

while True:
    print("Select an option:")
    print("1. Input mark for a course")
    print("2. List Courses")
    print("3. List students")
    print("4. Show student marks for a given course")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_mark()
    elif choice == "2":
        list_courses()
    elif choice == "3":
        list_students()
    elif choice == "4":
        show_mark()
    elif choice == "5":
        break
    else:
        print("Invalid choice")





