class Person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print(f"Name = {self.name}\nAge = {self.age}")

class Student(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender
    def displayStudent(self):
       self.displayPerson()
       print(f"Gender = {self.gender}")

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print(f"ID = {self.Id}")

s=Student("Diana",35,"female")
s.displayStudent()

e=Employee("Diana",35,100)
e.displayEmployee()
