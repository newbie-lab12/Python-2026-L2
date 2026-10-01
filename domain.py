from .student import Student
from .course import Course
from .mark import Mark

__all__ = ['Student', 'Course', 'Mark']
class Course:
    def __init__(self, idc: int, namec: str, credits: int):
        self.idc = idc
        self.namec = namec
        self.credits = credits

    def __str__(self):
        return f"Course ID: {self.idc:<6} | Name: {self.namec:<20} | Credits: {self.credits}"
      class Student:
  def __init__(self, sid: int, name: str, dob: str):
        self.id = sid
        self.name = name
        self.dob = dob
        self.gpa = 0.0

  def __str__(self):
      return f"ID: {self.id:<6} | Name: {self.name:<20} | DoB: {self.dob:<12} | GPA: {self.gpa:.2f}
