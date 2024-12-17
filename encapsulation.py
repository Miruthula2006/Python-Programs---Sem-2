class Student:
    id=int(input())#(public)(or) __id=123(private)
    __age=int(input())
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender# here it is private
    def display(self):
        print("Name = ",self.__name)
        print("Gender = ",self.gender)#here it is public(error)
s=Student("Anu","female")
s.display()
print(s.id)
print(s.age)
