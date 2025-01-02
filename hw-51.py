#1
class Count:
    def __init__(self,string):
        self.string=string
    def count_characters(self):
        alpha_count=0
        num_count=0
        special_count=0
        for i in self.string:
            if i.isalpha():
                alpha_count+=1
            elif i.isdigit():
                num_count+=1
            else:
                special_count+=1
        print(f"Alphabetic Characters: {alpha_count}")
        print(f"Numeric Characters: {num_count}")
        print(f"Special Characters: {special_count}")
string=input("Enter the String ")
c=Count(string)
c.count_characters()

#2
class Validation:
    def __init__(self,string):
        self.string=string
    def validate(self):
        alpha_count=0
        special_count=0
        for i in self.string:
            if i.isalpha():
                alpha_count+=1
            if not i.isalnum():
                special_count+=1
        if alpha_count>=1 and special_count>=1:
            print("The string contains both alphabets and special characters.")
        else:
            print("The string does not contains both alphabets and special characters.")
string=input("Enter the String: ")
v=Validation(string)
v.validate()
        
        


