#1
a = [1, 2, 4, 5]
n = len(a) + 1  
expected_sum = n * (n + 1) // 2
actual_sum = sum(a)
missing_number = expected_sum - actual_sum
print("Missing number is:", missing_number)
#2
arr = [4, 3, 2, 7, 8, 2, 3]
duplicates = []

for num in arr:
    if arr.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate numbers are:", duplicates)
#3
arr = [1, 2, 3, 4]
is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print("Array is sorted:", is_sorted)
#4
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
for num in arr:
    if arr.count(num) > len(arr) // 2:
        print("Majority element is:", num)
        break
 #5
is_balanced = False
for i in range(len(arr)): 
          total_sum -= arr[i]
          if left_sum == total_sum: 
                   is_balanced = True 
                  break 
           left_sum += arr[i]
 print("Is the array balanced?:", is_balanced)
#6
arr = list(map(int, input("Enter the array elements: ").split()))
target = int(input("Enter the target sum: ")) 
pairs = [] 
for i in range(len(arr)):
      for j in range(i + 1, len(arr)): 
                if arr[i] + arr[j] == target:
                          pairs.append((arr[i], arr[j]))
 print("Pairs that sum to", target, "are:", pairs)
