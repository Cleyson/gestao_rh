class Employee():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


emp = Employee('R 2 H G C')

print(emp.get_name())
