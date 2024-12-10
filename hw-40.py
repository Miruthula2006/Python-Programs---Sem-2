class Camera:
    def __init__(self, resolution):
        self.resolution = resolution  
    def take_photo(self):
        print("Taking a photo with resolution:", self.resolution)
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def make_call(self, number):
        print(f"A call to {number} ")  
    def send_message(self, number, message):
        print(f"Sending message: {message} to {number} ")
class Smartphone(Camera, Phone):
    def __init__(self, resolution, phone_number, brand, model):
        Camera.__init__(self, resolution)  
        Phone.__init__(self, phone_number)  
        self.brand = brand  
        self.model = model  
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Camera Resolution: {self.resolution}")
p = Smartphone("12 MP", 6356749614, "TechBrand", "X1")
p.display()




class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def student_info(self):
        print(f"Student Name: {self.name}\nCourse: {self.course}")
class StudentAthlete(Student):
   def __init__(self,name,course,sport):
       super().__init__(name,course)
       self.sport=sport
   def display_Athlete_info(self):
        self.student_info()
        print(f"Sports Name: {self.sport}")
s=StudentAthlete("Miruthula","AI","Tennis")
s.display_Athlete_info()

