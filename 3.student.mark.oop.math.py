import math
import numpy as np

students = []
courses = []
mark = []

def input_student():
    numberS = int(input('Number of students: '))
    for _ in range(numberS):
        sid = int(input('Student ID: '))
        name = input('Name of student: ')
        dob = input('Date of birth: ')
        students.append({'id': sid, 'name': name, 'dob': dob})

def input_courses():
    numberC = int(input('Number of courses: '))
    for _ in range(numberC):
        idc = int(input('Course ID: '))
        namec = input('Course name: ')
        credits = int(input('Credits: '))
        courses.append({'idc': idc, 'namec': namec, 'credits': credits})

def input_mark():
    sid = int(input('Student ID: '))
    idc = int(input('Course ID: '))
    raw_mark = float(input('Enter score: '))
    # Floor to 1 decimal place: floor(score * 10) / 10
    floored_mark = math.floor(raw_mark * 10.0) / 10.0
    mark.append({'id': sid, 'idc': idc, 'mark': floored_mark})

def calculate_gpa(student_id):
    student_marks = []
    course_credits = []
    
    # Map courses by ID for quick credit retrieval
    credits_map = {c['idc']: c['credits'] for c in courses}
    
    for m in mark:
        if m['id'] == student_id and m['idc'] in credits_map:
            student_marks.append(m['mark'])
            course_credits.append(credits_map[m['idc']])
            
    if not student_marks:
        return 0.0

    # NumPy weighted sum calculation
    marks_arr = np.array(student_marks)
    credits_arr = np.array(course_credits)
    
    total_credits = np.sum(credits_arr)
    if total_credits == 0:
        return 0.0
        
    weighted_sum = np.sum(marks_arr * credits_arr)
    return round(float(weighted_sum / total_credits), 2)

def list_students_by_gpa():
    if not students:
        print('No students available.')
        return
        
    for s in students:
        s['gpa'] = calculate_gpa(s['id'])
        
    # Sort descending by GPA
    sorted_students = sorted(students, key=lambda x: x['gpa'], reverse=True)
    
    print('\n--- Students Ranked by GPA ---')
    for s in sorted_students:
        print(f"ID: {s['id']} | Name: {s['name']} | GPA: {s['gpa']}")

def list_courses():
    for c in courses:
        print(f"Course ID: {c['idc']} | Name: {c['namec']} | Credits: {c['credits']}")

def list_students():
    for s in students:
        print(f"Student ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_mark():
    course_id = int(input('Enter course ID to get marks: '))
    found = False
    for m in mark:
        if m['idc'] == course_id:
            student = next((s for s in students if s['id'] == m['id']), None)
            course = next((c for c in courses if c['idc'] == course_id), None)
            if student and course:
                print(f"Student: {student['name']}, Course: {course['namec']}, Mark: {m['mark']}")
                found = True
    if not found:
        print('No marks found for this course.')

while True:
    print('\n--- MENU ---')
    print('1: Input students')
    print('2: Input courses')
    print('3: Input marks')
    print('4: List courses')
    print('5: List students')
    print('6: Show course marks')
    print('7: List students sorted by GPA')
    print('8: Exit')
    
    choice = input('Choose an option: ')
    
    if choice == '1':
       input_student()
    elif choice == '2':
        input_courses()
    elif choice == '3':
        input_mark()
    elif choice == '4':
        list_courses()
    elif choice == '5':
        list_students()
    elif choice == '6':
        show_student_mark()
    elif choice == '7':
        list_students_by_gpa()
    elif choice == '8':
        print('Exiting program.')
        break
    else:
        print('Invalid option. Please try again.')
