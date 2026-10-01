import math
from domains import Student, Course, Mark

def input_students(students_list):
    count = int(input("Enter number of students: "))
    for _ in range(count):
        sid = int(input("  Student ID: "))
        name = input("  Student name: ")
        dob = input("  Date of birth (DD/MM/YYYY): ")
        students_list.append(Student(sid, name, dob))

def input_courses(courses_list):
    count = int(input("Enter number of courses: "))
    for _ in range(count):
        idc = int(input("  Course ID: "))
        namec = input("  Course name: ")
        credits = int(input("  Course credits: "))
        courses_list.append(Course(idc, namec, credits))

def input_marks(marks_list, students_list, courses_list):
    if not students_list or not courses_list:
        print("Please enter students and courses first.")
        input("Press Enter to continue...")
        return

    sid = int(input("Enter student ID: "))
    idc = int(input("Enter course ID: "))
    raw_mark = float(input("Enter mark: "))
    floored_mark = math.floor(raw_mark * 10.0) / 10.0
    marks_list.append(Mark(sid, idc, floored_mark))
