class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Developer(Employee):

    def developer(self):
        super().__init__(self.name,self.salary)
        self.programming_language = "Python"

class Manager(Employee):

    def manager(self):
        super().__init__(self.name,self.salary)
        self.team_size = 10

e=Employee("Srinivas",50000)

d=Developer("Alice",60000)
d.developer()
print("Developer Name:",d.name)
print("Developer Salary:",d.salary)
print("Programming Language:",d.programming_language)

m=Manager("Bob",70000)
m.manager()
print("Manager Name:",m.name)
print("Manager Salary:",m.salary)
print("Team Size:",m.team_size)