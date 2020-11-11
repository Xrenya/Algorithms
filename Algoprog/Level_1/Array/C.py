number = int(input())
arr = [int(x) for x in input().split()]

def bigger(arr):
    counter = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            counter += 1
    return counter
    
print(bigger(arr))
