class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter ID:")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID = ",self.id,"Name = ",self.name)
#inherited the Employee class
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()#will go to the particular method
        self.sal=int(input("Enter the Salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()#will go to the particular method
        print("salary = ",self.sal)
#object creation
p=Perks()
p.getDetails()
p.displayInfo()        
    
        
        
