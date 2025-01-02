class Addition:
    def add(self,a,b,c=0):
        result=0
        result=a+b+c
        return result
ad=Addition()
ans=ad.add(2,3)
print(ans)
ans1=ad.add(1,2,3)
print(ans1)
