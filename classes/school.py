from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
    
    def list_students(self):
        for i, object in enumerate(self.students):
            print(f'{i + 1}. {object.name} {object.school_id}')
        
    def find_student_by_id(self, student_id):
        for object in self.students:
            if object.school_id == student_id:
                return object



