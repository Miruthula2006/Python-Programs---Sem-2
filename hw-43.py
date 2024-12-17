class Student:
    def __init__(self):
        self.id = input("Enter ID: ")
        self.name = input("Enter Name: ")
        self.grade = input("Enter Grade: ")
    def validate_details(self):
        if len(self.id) == 7 and self.id[:3] == "STU" and self.id[3:].isdigit():
            print("ID is Valid")
        else:
            print("ID is Invalid")

        if len(self.name) >= 2 and all(char.isalpha() or char.isspace() for char in self.name):
            print("Name is Valid")
        else:
            print("Name is Invalid")

        if self.grade[0].isdigit() and self.grade.endswith("th Grade")  or self.grade.endswith("st Grade") or  self.grade.endswith("rd Grade") and int(self.grade[:-8]) in range(1,13):
        
            print("Grade is Valid")
        else:
            print("Grade is Invalid")
    def display_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
stu = Student()
stu.validate_details()
stu.display_details()
