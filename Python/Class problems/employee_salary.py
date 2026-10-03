class Employee:

    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display(self):
        print("Name :",self.name)
        print("salary :",self.salary)
        print("Department :",self.department)

    def annual_salary(self):
        print("Annual Salary :",self.salary*12)

e1=Employee("Srinivas",50000,"Python Developer")
e2=Employee("Suma",75000,"Java Developer")

e1.display()
e1.annual_salary()
e2.display()
e2.annual_salary()
