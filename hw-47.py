roman_symbols=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
symbol=input("Enter the symbol: ")
result=0
for v,s in roman_symbols:
    for n in symbol:
        if n==v:
            result += s
print(result) 
