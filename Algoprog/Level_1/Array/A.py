number = int(input())
arr = []
even = []
for i in range(number):
    arr.append(int(input()))
    if i%2 == 0:
        even.append(str(arr[i]))
    
print(" ".join(even))
