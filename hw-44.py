#1
w1=input()
w2=input()
merged_string = []
l1, l2 = len(w1), len(w2)
max_len = max(l1, l2)
for i in range(max_len):
    if i < l1:
        merged_string.append(w1[i])
    if i < l2:
        merged_string.append(w2[i])
print( ''.join(merged_string))

#2
flowerbed=list(map(int, input().split()))
n=int(input())
count=0
l=len(flowerbed)
for i in range(l):
    if flowerbed[i]==0:
        left=(i==0) or (flowerbed[i-1]==0)
        right=(i==l-1) or (flowerbed[i+1]==0)
        if left and right:
            flowerbed[i]=1
            count+=1
            if count>=n:
                print("True")
                break
else:
    print("False")

