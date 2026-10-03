class Student:

    def __init__(self,name,maths,python,database):
        self.name=name
        self.maths=maths
        self.python=python
        self.database=database

    def total(self):
        return self.maths + self.python + self.database

    def average(self):
        return self.total()/3

    def result(self):
        if self.maths >=40 and self.python >=40 and self.database >=40:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Srinivas",85,90,75)

print("Total :",s1.total())
print("Average :",round(s1.average(),2))
print("Result :",s1.result())