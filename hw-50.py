class calculator:
    def __init__(self,num1,num2,operation):
        self.num1=num1
        self.num2=num2
        self.operation=operation
        if self.operation=="/" and self.num2==0:
            raise ZeroDivisionError("Zero Division Error please Retry")
        if operation not in ("+","-","*","/"):
            raise KeyError("Invalid input please Retry")
    def calculate(self):
        if self.operation=="+":
            print(self.num1+self.num2)
        elif self.operation=="-":
            print(self.num1-self.num2)
        elif self.operation=="*":
            print(self.num1*self.num2)
        elif self.operation=="/":
            print(self.num1/self.num2)
        else:
            raise TypeError("Unexpected Error try again later")
try:
    num1=int(input("Enter the number: "))
    num2=int(input("Enter the number: "))
    operation=input("Enter the operation to be performed: ")
    c=calculator(num1,num2,operation)
    c.calculate()
except Exception as e:
    print(e)
        
        
        
