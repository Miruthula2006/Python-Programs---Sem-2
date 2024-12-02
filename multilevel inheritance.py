class Person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print(f"Name = {self.name}\nAge = {self.age}")
class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print(f"ID = {self.Id}")
class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age,Id)
        self.salary=salary
    def displayManager(self):
        self.displayEmployee()
        print(f"Salary = {self.salary}")
m=Manager("Diana",35,100,50000)
m.displayManager()
