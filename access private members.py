#To access private members
class Employee:
    def __init__(self,name,salary):
        self.name=name#public variable
        self.__salary=salary#private variable
e=Employee("Ana",100000)
print("Name = ",e.name)
print("Salary = ",e._Employee__salary)

#using inheritance

class Employee:
    def __init__(self,name,age,salary):
        self.__name=name
        self.__age=age#private
        self.salary=salary
    def display(self):
        print("Name : ",self.__name)
        print("Age : ",self.age)#public
        print("Salary : ",self.salary)
e=Employee("Ana",25,100000)
e.display()
