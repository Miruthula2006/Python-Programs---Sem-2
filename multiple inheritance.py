class Employee:
    def __init__(self,name,Id,position):
        self.name=name
        self.Id=Id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name: {self.name}\nId: {self.Id}\nPosition: {self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayAddressInfo(self):
        print(f"Street: {self.street}\nState: {self.state}\nCountry: {self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)#super allows to initialize the variables i.e:name,Id,position(can only use once in first class)
        Address.__init__(self,street,state,country)#other way instead of using super
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayAddressInfo()
ed=EmployeeDetails("Anu",100,"Manager","Shenoy Nagar","TamilNadu","India")
ed.displayEmp()







































