class Student:
    _id_counter =1

    def __init__(self,name):
        self.student_id =Student._id_counter
        Student._id_counter +=1
        self.name = name
        self.grades ={}
        self.enrolled_courses =[]
    def __str__(self):
        return f"student ID : {self.student_id}, Nsme : {self.name} , Grades : {self.grades}"
    
    def __repr__ (self):
        return f"student ID : {self.student_id}, Nsme : {self.name} , Grades : {self.grades}"
    
    def add_grade(self,course_id,grade):
        if not 0<= grade <=100 :
            raise ValueError("grades must be between 0 and 100")
        self.grades[course_id] =grade 
    def enrool_in_course(self,course):
        if course in self.enrolled_courses:
            print(f"{self.name} is already enrolled in {course}")
        self.enrolled_courses.append(course)

