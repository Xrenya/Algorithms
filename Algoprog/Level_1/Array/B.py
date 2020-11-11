number = int(input())
arr = []
for i in range(number):
    num = int(input())
    if num%2 == 0:
        arr.append(str(num))
        
print(" ".join(arr))
