class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_possition(position):
        valid_possition = ['manager', 'chasier', 'cook']
        return position in valid_possition


# staticmethod
print(Employee.is_valid_possition('cook'))

# instance method 
employe1 = Employee('habil', 'manager')
employe2 = Employee('kabil', 'cook')
employe3 = Employee('Bobil', 'chasier')

print(employe1.get_info())
print(employe2.get_info())
print(employe3.get_info())