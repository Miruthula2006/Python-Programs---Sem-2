#1
def reverse(s):
    if len(s)<=1:
        return s
    else:
        return reverse(s[1:])+s[0]
user_input=input("Enter the String to reverse:")
reverse=reverse(user_input)
print("Reversed string:",reverse)
#2
def  is_palindrome(s):
    s=s.lower()
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

s=input("Enter the string:")
print(is_palindrome(s))
#3
x=int(input("Enter base")) 
n=int(input("Enter power")) 
def power(x,n): 
        if n==0: 
                return 1 
        else:
                return x*power(x, n-1) 
res=power(x,n) 
print(res)
#4
def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total
print(sum_of_digits(2023))
#5
n=int(input("Enter the number of elements in the array"))
arr=[]
tot=0
for i in range(n):
 e=list(map(int,input().split()))
 arr.append(e)
for i in range(n):
 for j in range(n):
     print(arr[i][j],end=" ")
     print()
for i in range(n):
 for j in range(n):
     tot+=arr[i][j]
print(tot)
#6
n=int(input("Enter the number of elements in the array:"))
arr=[]
for i in range(n):
 e=list(map(int,input().split()))
 arr.append(e)
print("Original matrix")
for i in range(n):
 for j in range(n):
     print(arr[i][j],end=" ")
     print()
print("Transpose")
for i in range(n):
 for j in range(n):
     print(arr[j][i],end=" ")
print()

