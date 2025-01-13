from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name):
         self.name=name
    @abstractmethod
    def calculate_pay(self):
         pass
class SalariedEmployee:
    def __init__(self,name,annual_salary):
         self.name=name
         self.annual_salary=annual_salary
    def calculate_pay(self):
         return self.annual_salary/12
class HourlyEmployee:
    def __init__(self,name,hoursworked,hourlyrate):
        self.name=name
        self.hoursworked=hoursworked
        self.hourlyrate=hourlyrate
    def calculate_pay(self):
         return self.hoursworked*self.hourlyrate
se_name=input("Enter the name: ")
amount=float(input("Enter the annual amount: "))
s=SalariedEmployee(se_name,amount)
print(f"Salaried Employee: {se_name} Pay: {s.calculate_pay():.2f}")

he_name=input("Enter the name: ")
hours_worked=float(input("Enter how many hours worked: "))
hourly_rate=float(input("Enter the hourly rate: "))
hour=HourlyEmployee(he_name,hours_worked,hourly_rate)
print(f"Hourly Employee: {he_name} Pay: ${hour.calculate_pay():.2f}")
