class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(400)
b2=Book(600)
print("Total number of Pages : ",b1+b2)
