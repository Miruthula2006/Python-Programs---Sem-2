class Student:
    def __init__(self,name=""):
        self.name=name
    def getData(self):
        self.ID=input("Enter ID")
    def display(self):
        print("Student detail")
        print("Name=",self.name)
        print("ID=",self.ID)
s_name=input("Enter the name")
s=Student(s_name)
s.getData()
s.display()
