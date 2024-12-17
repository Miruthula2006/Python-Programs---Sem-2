class Library:
    def issue_book(self,book_name,user):
        return f"Book Issued is {book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is {book_name} by {user}"

class DigitalLibrary:
    def issue_book(self,book_name,user):
        return f"Book Issued is {book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is {book_name} by {user}"

lib=Library()
dig=DigitalLibrary()
print("*****LIBRARY*****")
lib_book=input()
lib_username=input()
print(lib.issue_book(lib_book,lib_username))
print(lib.returned_book(lib_book,lib_username))

dig_book=input()
dig_username=input()
print(dig.issue_book(dig_book,dig_username))
print(dig.returned_book(dig_book,dig_username))

