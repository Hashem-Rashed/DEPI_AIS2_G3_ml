from student import Student
from course import Course
class SystemManager:
    
    def __init__(self):
        self.students = {}
        self.courses = {}
        
    def add_student(self, name):
        student =  Student(name)
        self.students[student.student_id] = student
        print(f"student added successfully!.")
        return student.student_id
    def remove_student(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            for course in list(student.enrolled_courses):
                course.remove(student)
            del self.students[student_id]
            print("student removed successfully.")
        else:
            print("Invalid student id")