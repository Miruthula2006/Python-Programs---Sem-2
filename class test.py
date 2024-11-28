class Inventory():
    def __init__(self):
        self.prodId=int(input("Enter the Product ID: "))
        self.prodName=input("Enter the Product Name: ")
        self.prodCount=int(input("Enter the product Count: "))
class Products(Inventory):
    def display(self):
        print("Product Id: ",self.prodId)
        print("Product Name: ",self.prodName)
        print("Product Count: ",self.prodCount)
p=Products()
p.display()




class Inventory():
    def __init__(self,proId,prodName,prodCount):
        self.prodId=proId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product Id: ",self.prodId)
        print("Product Name: ",self.prodName)
        print("Product Count: ",self.prodCount)
p=Inventory(12,"Pencil",100)
p.display()
