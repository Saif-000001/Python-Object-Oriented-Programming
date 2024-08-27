class Student:

    # class variables 
    class_year = 2025
    class_student = 0

    def __init__(self, name, age):
        # instances variables
        self.name = name
        self.age = age  
        Student.class_student += 1

st1 = Student('Habil', 23)
st2 = Student('Kabil', 22)

print(f"{st1.name} {st1.age}")
print(f"{st2.name} {st2.age}")

print(f"My graduating class of {Student.class_year} has {Student.class_student} students")