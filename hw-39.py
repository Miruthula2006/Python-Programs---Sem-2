#1
class Library:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre
    def displayBookInfo(self):
        print(f"Name: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}")
class Member:
    def __init__(self, m_name, m_id):
        self.m_name = m_name
        self.m_id = m_id
    def displayMemberInfo(self):
        print(f"Member Name: {self.m_name}\nMember ID: {self.m_id}")
class LibraryManagement(Library, Member):
    def __init__(self, name,author,genre,m_name,m_id ):
        super().__init__(name,author,genre)
        Member.__init__(self, m_name, m_id)
    def display(self):
        self.displayBookInfo()
        self.displayMemberInfo()
l = LibraryManagement("A Game of Thrones","George R.R. Martin","Fantasy","Ana",45)
l.display()


#2
class Restaurant:
    def __init__(self,name,menu,price):
       self.name=name
       self.menu=menu
       self.price=price
    def displayRestaurantInfo(self):
       print(f"Restaurant Name: {self.name}\nMenu: {self.menu}\nPrice: {self.price}")
class Delivery:
    def __init__(self,rider_name,rider_number):
       self.rider_name=rider_name
       self.rider_number=rider_number
    def displayDeliveryInfo(self):
       print(f"Delivery Person: {self.rider_name}\nDelivery Person Contact: {self.rider_number}")
class Order(Restaurant,Delivery):
    def __init__(self,name,menu,price,rider_name,rider_number):
       super().__init__(name,menu,price)
       Delivery.__init__(self,rider_name,rider_number)
    def displayOrder(self):
       self.displayRestaurantInfo()
       self.displayDeliveryInfo()

d=Order("A2B","Chicken Rice",150,"James",1234506789)
d.displayOrder()
