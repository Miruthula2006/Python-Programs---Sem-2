class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
           self.balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
           self.balance-=amount
        else:
           print("Not Having Enough Balance")
    def check_balance(self):
           print(f"Your Balance is {self.balance}")
A1=BankAccount("Anu",1230984576,20000)
A1.deposit(1000)
A1.withdraw(10000)
A1.check_balance()


class Cosmetics:
    def __init__(self,name="kajal",brand="lakme",price=150,category="Makeup"):
        self.name=name
        self.brand=brand
        self.price=price
        self.category=category
    def show(self):
        print(f"Name = {self.name}\nBrand = {self.brand}\nPrice = {self.price}\nCategory = {self.category}")
p1=Cosmetics("Lipstick", "L'Oreal",300, "Makeup")
p1.show()
p=Cosmetics()
p.show()
