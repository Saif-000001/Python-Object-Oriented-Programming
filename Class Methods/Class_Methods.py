class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    # Instance Methods
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def student_count(cls):
        return f"Total of the students : {cls.count}"
    
    @classmethod
    def student_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/ cls.count}"

student1 = Student('habil', 3.15)
student2 = Student('kabil', 3.18)
student3 = Student('babil', 3.53)

print(Student.student_count())
print(Student.student_avg_gpa())