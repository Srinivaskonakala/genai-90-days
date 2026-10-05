students=[]

def add_student():
    name=input("Enter name:")
    roll_number=input("Enter roll number:")
    marks=list(map(int,input().split()))
    student={
        "name" : name,
        "roll_number" : roll_number,
        "marks" : marks
    }
    students.append(student)

    print("Student Data Added Successfully!")

def display_students():
    if len(students)==0:
        print("No student data found.")
        return
    
    for student in students:
        print("\nName:",student['name'])
        print("Roll Number:",student['roll_number'])
        print("Marks:",student['marks'])

def search_student():
    roll_number=input("Enter roll number to search: ")
    for student in students:
        if student['roll_number']==roll_number:
            print("\nStudent Found!")
            print("Name:",student['name'])
            print("Roll Number:",student['roll_number'])
            print("Marks:",student['marks'])
            return
        
        print("Student not found.")

def calculate_average():
    roll_number=input("Enter the roll number to calculate: ")
    for student in students:
        if student['roll_number']==roll_number:
            marks=student['marks']
            average=sum(marks)/len(marks)

            print("Average:",int(average))
            print("Grade:",get_grade(average))

        else:
            print("Student not found.")

def get_grade(average):
    if average>=90:
        return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"

while True:
    print("\n=====Student Management System=====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        add_student()
    elif choice==2:
        display_students()
    elif choice==3:
        search_student()
    elif choice==4:
        calculate_average()
    elif choice==5:
        print("Thank You!")
        break

    else:
        print("Invalid choice!")
