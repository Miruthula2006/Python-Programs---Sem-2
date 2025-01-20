import array as arr
n = arr.array('i')
x = int(input("Enter the number of elements: "))
for i in range(x):
    n.append(int(input("Enter an element: ")))
l = []
for num in n:
    if num == 0:
        l.append(num)  
for num in n:
    if num != 0:
        l.append(num)  
print(l)
#another method
n=int(input()) # no of elements in the array - 5
l=[] # empty list 
for i in range(n): 
    a=int(input())
    l.append(a) # 1 2 5 0 0 
non_zero_index = 0
for i in range(len(l)): # i=4 ,non=3
    if l[i]!=0: # l[0]!=0 , l[1]!=0 , l[2]!=0 , l[3]!=0 , l[4]!=0
        l[non_zero_index],l[i]=l[i],l[non_zero_index] # l[0],l[0]=l[0],l[0], l[1],l[2]=l[2],l[1] , l[2],l[4]=l[4],l[2]
        non_zero_index += 1 # non-3
print("Updated array:", l)
#next question
prices = [7, 1, 5, 3, 6, 4]
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
print(profit)

