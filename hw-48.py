import re
from random import randint
class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def validate_email(self):
        pattern = r'^[a-z0-9_.+]+@gmail\.com$'
        if re.match(pattern, self.email):
            print("Valid Email ID")
        else:
            print("Invalid Email ID")
    def generate_member_id(self):
        self.member_id = f"LIB{randint(1000, 9999)}"
        return self.member_id
    def verify_member_id(self):
        if self.member_id and self.member_id.startswith("LIB") and self.member_id[3:].isdigit():
            return "Member ID is Valid"
        else:
            return "ID not Valid"
class Library(Member):
    def __init__(self, name, email):
        super().__init__(name, email)
    def manage_books(self):
        self.book_id = int(input("Enter Book ID: "))
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Book Author: ")
        print(f"Book added: {self.title} by {self.author} ID: {self.book_id}")
    def register_members(self):
        member_id = self.generate_member_id()
        print(f"Member Registered with ID: {member_id}")
        print(self.verify_member_id())
    def borrowed_book(self):
        if self.book_id:
            print(f"Borrowed Book: {self.title} by {self.author}")
    def return_book(self):
        if self.book_id:
            print(f"Returned Book: {self.title} by {self.author}")
m = Member("Miruthula", "miruthulam2006@gmail.com")
m.validate_email()
m.generate_member_id()
m.verify_member_id()
l = Library("Miruthula", "miruthulam2006@gmail.com")
l.register_members()
l.manage_books()
l.borrowed_book()
l.return_book()




