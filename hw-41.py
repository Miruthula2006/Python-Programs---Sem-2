#1
class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def displayVehicleInfo(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year, doors, capacity):
        super().__init__(make, model, year)
        self.doors=doors
        self.capacity=capacity
    def displayCarInfo(self):
        super().displayVehicleInfo()
        print(f"Number of Doors: {self.doors}\nTrunk Capacity: {self.capacity}")
class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, axles):
        super().__init__(make,model, year)
        self.cargo_capacity=cargo_capacity
        self.axles=axles
    def displayTruckInfo(self):
        print(f"Cargo Capacity: {self.cargo_capacity}")
        print(f"Number of Axles: {self.axles}")
class PickupTruck(Car,Truck):
    def __init__(self, make, model, year, doors, capacity,cargo_capacity, axles):
        Vehicle.__init__(self,make, model, year)
        self.doors=doors
        self.capacity=capacity
        self.cargo_capacity=cargo_capacity
        self.axles=axles
    def displayPickupTruck(self):
        self.displayCarInfo()
        self.displayTruckInfo()
v=PickupTruck("Toyota","Hilux",2024,4,450,3,2)
v.displayPickupTruck()

#2
class Product:
    def __init__(self,product_ID,name,price):
        self.product_ID=product_ID
        self.name=name
        self.price=price
    def displayProductInfo(self):
        print(f"Product ID = {self.product_ID}\nName = {self.name}\nPrice = Rs.{self.price}")
class Electronics(Product):
    def __init__(self,product_ID,name,price,warranty,brand):
        super().__init__(product_ID,name,price)
        self.warranty=warranty
        self.brand=brand
    def displayElectronicsInfo(self):
        self.displayProductInfo()
        print(f"Warranty Period = {self.warranty} year\nBrand = {self.brand}")
class Clothing(Product):
    def __init__(self,product_ID,name,price,size,material):
        super().__init__(product_ID,name,price)
        self.size=size
        self.material=material
    def displayClothingInfo(self):
        self.displayProductInfo()
        print(f"Size = {self.size}\nMaterial = {self.material}")
e=Electronics(121,"Phone",32000,1,"Redmi")
e.displayElectronicsInfo()
c=Clothing(212,"Pant",800,32,"Cotton")
c.displayClothingInfo()

        
