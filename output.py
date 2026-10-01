import curses

def display_in_curses(title: str, lines: list):
    def _render(stdscr):
        curses.curs_set(0)
        stdscr.clear()


        stdscr.addstr(1, 2, f"=== {title} ===", curses.A_BOLD | curses.A_UNDERLINE)

       
        row = 3
        if not lines:
            stdscr.addstr(row, 2, "No data available.")
            row += 1
        else:
            for line in lines:
                stdscr.addstr(row, 2, line)
                row += 1

        stdscr.addstr(row + 1, 2, "Press any key to return to menu...", curses.A_DIM)
        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(_render)

def show_students(students_list):
    lines = [str(s) for s in students_list]
    display_in_curses("STUDENT LIST", lines)

def show_courses(courses_list):
    lines = [str(c) for c in courses_list]
    display_in_curses("COURSE LIST", lines)

def show_student_marks(course_id: int, marks_list, students_list, courses_list):
    course = next((c for c in courses_list if c.idc == course_id), None)
    course_name = course.namec if course else f"ID {course_id}"
    
    lines = []
    for m in marks_list:
        if m.idc == course_id:
            student = next((s for s in students_list if s.id == m.sid), None)
            name = student.name if student else f"Student ID: {m.sid}"
            lines.append(f"Student: {name:<20} | Mark: {m.mark:.1f}")

    display_in_curses(f"MARKS FOR COURSE: {course_name}", lines)

def show_sorted_gpa(students_list):
    lines = [f"Rank {idx + 1}: {s.name:<20} (ID: {s.id}) — GPA: {s.gpa:.2f}" 
             for idx, s in enumerate(students_list)]
    display_in_curses("STUDENTS RANKED BY GPA (DESCENDING)", lines)
