class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print(f"Name = {self.name}\nAge = {self.age}")

class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"Employee Id = {self.eid}")

class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        print(f"Department = {self.dept}")

class Teamleader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamleaderInfo(self):
        self.displayManagerInfo()
        self.displayDeveloperInfo()
        print(f"Teamsize = {self.teamsize}")

e=Teamleader("Anu",25,143,"IT",5)
e.displayTeamleaderInfo()



class hardware
