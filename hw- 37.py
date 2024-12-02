class Student:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def __del__(self):
        print("The object has been deleted")
    def show(self):
        print("Student Information")
        print(f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}\nGrade: {self.grade}")
stu=Student("Anu",18,"Computer Science","A")
stu.show()
del stu

class Student:
    def __init__(self,name,roll_no,m1,m2,m3):
        self.name=name
        self.roll_no=roll_no
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.percentage=((m1+m2+m3)/300)*100
    def show(self):
        if self.percentage >= 85:
           print("grade S")
        elif percentage >= 75:
           print("grade A")
        elif percentage >= 65:
           print("grade B")
        elif percentage >= 55:
           print("grade C")
        elif percentage >= 50:
           print("grade D")
        else:
           print("grade F")
s=Student("Miruthula",29,90,89,87)
s.show()
    


