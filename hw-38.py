#1
class Person:
    def getPersonInfo(self):
        self.name=input("Enter Name: ")
    def show_name(self):
        print("Name = ",self.name)
class Student(Person):
    def getId(self):
        self.getPersonInfo()
        self.id=input("Enter ID: ")
    def show_student_id(self):
        self.show_name()
        print("ID = ",self.id)
s=Student()
s.getId()
s.show_student_id()

#2
class Employee:
    def getEmployeeInfo(self):
        self.name=input("Enter the name: ")
        self.salary=int(input("Enter the Salary: "))
    def display_details(self):
        print("Name = ",self.name)
        print("salary = ",self.salary)
class Manager(Employee):
    def getdept(self):
        self.getEmployeeInfo()
        self.dept=input("Enter the department: ")
    def display_department(self):
        self.display_details()
        print("Department = ",self.dept)
m=Manager()
m.getdept()
m.display_department()

