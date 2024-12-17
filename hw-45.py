#1
class System:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def set_password(self):
        if len(self.__password) < 8:
            print("Password must be at least 8 characters long")
            return False
        if not any(char.isdigit() for char in self.__password):
            print("Password must contain at least one number")
            return False
        if not any(char in "!@#$%^&*()-_+=<>?/|\\{}[]:;\"\'" for char in self.__password):
            print("Password must contain at least one special character")
            return False
        return True
    def check_password(self):
        if self.set_password()==True:
            print("Password is valid")
        else:
            print("Password is Invalid")
username=input()
password=input()
s=System(username, password)
s.check_password()


#2
class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    def set_price(self, price):
        if price>0:
            self.__price=price
        else:
            print("Price must be greater than 0")
    def set_stock(self, stock):
        if stock==int(stock) and stock >= 0:
            self._stock = stock
        else:
            print("Stock must be a non-negative integer")
    def get_stock(self):
        return self.__stock
name=input("Enter the name")
price=int(input("Enter the price"))
stock=int(input("Enter the stock"))
p=Product(name,price,stock)
print(f"Stock:{p.get_stock()}")

#3
class Student:
    def __init__(self,name,age,marks):
        self.__name=name
        self.__age=age
        self.__marks=marks
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name=name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if 5<=age<= 100:
            self.__age = age
        else:
            raise ValueError("Age must be between 5 and 100")
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        if 0 <=marks<= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100")
try:
    name=input()
    age=int(input())
    marks=int(input())
    s=Student(name,age,marks)
    s.set_age(age)
    s.set_marks(marks)
    print(f"Name:{s.get_name()}\nAge:{s.get_age()}\nMarks:{s.get_marks()}")

except ValueError as e:
    print(e)

