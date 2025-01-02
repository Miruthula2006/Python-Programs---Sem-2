class Calculator:
    def calculate(self,a1,a2=0,a3=0):
        for i in (a1,a2,a3):
            if type(i) not in (int,float):
                raise ValueError("arguments should be integers or floats")
        if a1!=0 and a2==0 and a3==0:
            return a1*a1
        elif a1!=0 and a2!=0 and a3==0:
            return a1+a2
        else :
            return a1*a2*a3
try:
    c=Calculator()
    square=c.calculate(2)
    print(square)
    s=c.calculate(5,4)
    print(s)
    product=c.calculate("2",4,5)
    print(product)
except ValueError as e:
    print(e)



    

