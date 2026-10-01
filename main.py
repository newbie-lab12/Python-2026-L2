import numpy as np
from input import input_students, input_courses, input_marks
from output import show_students, show_courses, show_student_marks, show_sorted_gpa

students = []
courses = []
marks = []

def calculate_gpa(student_id: int) -> float:
    student_marks = []
    course_credits = []
    credit_map = {c.idc: c.credits for c in courses}

    for m in marks:
        if m.sid == student_id and m.idc in credit_map:
            student_marks.append(m.mark)
            course_credits.append(credit_map[m.idc])

    if not student_marks:
        return 0.0

    marks_arr = np.array(student_marks)
    credits_arr = np.array(course_credits)

    total_credits = np.sum(credits_arr)
    if total_credits == 0:
        return 0.0

    weighted_gpa = np.sum(marks_arr * credits_arr) / total_credits
    return round(float(weighted_gpa), 2)

def rank_students_by_gpa():
    for s in students:
        s.gpa = calculate_gpa(s.id)
    sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
    show_sorted_gpa(sorted_students)

def main():
    while True:
        print("\n=================================")
        print("    STUDENT MANAGEMENT SYSTEM    ")
        print("=================================")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses (curses)")
        print("5. List students (curses)")
        print("6. Show marks for a course (curses)")
        print("7. Rank students by GPA (curses)")
        print("8. Exit")

        choice = input("Enter choice [1-8]: ").strip()

        if choice == '1':
            input_students(students)
        elif choice == '2':
            input_courses(courses)
        elif choice == '3':
            input_marks(marks, students, courses)
        elif choice == '4':
            show_courses(courses)
        elif choice == '5':
            show_students(students)
        elif choice == '6':
            if not courses:
                print("No courses available.")
                continue
            cid = int(input("Enter course ID: "))
            show_student_marks(cid, marks, students, courses)
        elif choice == '7':
            rank_students_by_gpa()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == '__main__':
    main()
