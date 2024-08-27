class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
    
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)

        self.employees.append(new_employee)
    
    def list_employee(self):
        return [employee.get_details() for employee in self.employees]


company = Company('Kustory Resturant')

company.add_employee('habil', 'manager')
company.add_employee('kabil', 'water')
company.add_employee('babul', 'water')

# print(company.list_employee())
print(company.name)
for employee in company.list_employee():
    print(employee)


company1 = Company('Tawaa Resturant')

company1.add_employee('habil', 'manager')
company1.add_employee('kabil', 'water')
company1.add_employee('babul', 'water')

# print(company.list_employee())
print(company1.name)
for employee in company1.list_employee():
    print(employee)
